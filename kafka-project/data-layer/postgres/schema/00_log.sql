CREATE TABLE IF NOT EXISTS ServerLog (
	 id								BIGSERIAL			NOT NULL
	,request_host								VARCHAR(16)
	,request_user								VARCHAR(16)
	,request_time					TIMESTAMP		NOT NULL
	,request_status							SMALLINT			NOT NULL
	,request_bytes_sent						INTEGER
	,request_bytes_out						INTEGER
	,request_method				VARCHAR(8)		NOT NULL
	,request_endpoint				VARCHAR(255)	NOT NULL
	,request_http_version		VARCHAR(16)		NOT NULL
)
