with source as (
    select * 
    from {{ source('my_dbt_db', 'raw_orders') }}
),
renamed as (
    select
        id as order_id,         -- Renommage de la colonne 'id' en 'order_id'
        customer as customer_id, -- Renommage de la colonne 'customer' en 'customer_id'
        ordered_at,             -- Ajout de la colonne 'ordered_at'
        store_id                -- Ajout de la colonne 'store_id'
    from source
)
select * 
from renamed
