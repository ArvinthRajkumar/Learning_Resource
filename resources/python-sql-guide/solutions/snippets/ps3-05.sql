SELECT NULL = NULL AS equal_to_itself, NULL IS NULL AS is_null, 1 NOT IN (2, NULL) AS not_in_with_null, COALESCE(NULL, 'fallback') AS coalesced;
