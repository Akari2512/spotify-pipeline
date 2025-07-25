from pyathena import connect
import pandas as pd

conn = connect(
    s3_staging_dir = 's3://spotify-pipeline-akari/athena-result/',
    region_name = 'us-east-1' 
)

query = """
    SELECT 
        CASE
            WHEN released_year <= 1979 THEN 'vintage'
            WHEN released_year BETWEEN 1980 AND 1999 THEN 'retro'
            WHEN released_year BETWEEN 2000 AND 2009 THEN 'early_2000s'
            WHEN released_year BETWEEN 2010 AND 2019 THEN 'modern'
            WHEN released_year >= 2020 THEN 'current'
            ELSE 'unknown'
        END AS release_group,

        COUNT (*) AS song_count,
        ROUND(AVG(streams)) as avg_streams,
        ROUND(AVG(bpm), 1) as avg_bpm,
        ROUND(AVG(danceability), 2) as avg_danceability,
        ROUND(AVG(valence), 2) as avg_valence,
        ROUND(AVG(energy), 2) as avg_energy,
        ROUND(AVG(acousticness), 2) as avg_acousticness,
        ROUND(AVG(instrumentalness), 2) as avg_instrumentalness,
        ROUND(AVG(liveness), 2) as avg_liveness,
        ROUND(AVG(speechiness), 2) as avg_speechiness
    FROM spotify_db.spotify_2023
    GROUP BY 
        CASE
            WHEN released_year <= 1979 THEN 'vintage'
            WHEN released_year BETWEEN 1980 AND 1999 THEN 'retro'
            WHEN released_year BETWEEN 2000 AND 2009 THEN 'early_2000s'
            WHEN released_year BETWEEN 2010 AND 2019 THEN 'modern'
            WHEN released_year >= 2020 THEN 'current'
            ELSE 'unknown'
        END
    ORDER BY release_group

"""

query_top4_artists = """
    WITH artist_streams AS (
        SELECT
            CASE 
                WHEN released_year <= 1979 THEN 'vintage'
                WHEN released_year BETWEEN 1980 AND 1999 THEN 'retro'
                WHEN released_year BETWEEN 2000 AND 2009 THEN 'early_2000s'
                WHEN released_year BETWEEN 2010 AND 2019 THEN 'modern'
                WHEN released_year >= 2020 THEN 'current'
                ELSE 'unknown'
            END AS release_group,
    
            artists_name,
            SUM(streams) AS total_streams
        FROM spotify_db.spotify_2023
        GROUP BY 
            CASE 
            WHEN released_year <= 1979 THEN 'vintage'
            WHEN released_year BETWEEN 1980 AND 1999 THEN 'retro'
            WHEN released_year BETWEEN 2000 AND 2009 THEN 'early_2000s'
            WHEN released_year BETWEEN 2010 AND 2019 THEN 'modern'
            WHEN released_year >= 2020 THEN 'current'
            ELSE 'unknown'
            END,
            artists_name
    ),

    ranked_artists AS (
        SELECT *,
            ROW_NUMBER() OVER (
            PARTITION BY release_group 
            ORDER BY total_streams DESC
        ) AS rn
        FROM artist_streams
    )

    SELECT release_group, artists_name, total_streams
    FROM ranked_artists
    WHERE rn <= 4
    ORDER BY release_group, total_streams DESC;

"""

df = pd.read_sql(query, conn)

df_top4 = pd.read_sql(query_top4_artists, conn)

print(df.head(5))
print(df_top4)

df_top4.to_csv('data/processed/top4_artists_by_group.csv', index=False)
df.to_csv('data/processed/release_group_summary.csv', index=False)