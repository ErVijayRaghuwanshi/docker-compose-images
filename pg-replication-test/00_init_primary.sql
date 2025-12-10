DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'replicator') THEN

      CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'repl_password123';
   END IF;
END
$do$;

-- Additionally, you need to allow this user to connect for replication in
-- the pg_hba.conf file. The official PostgreSQL Docker image typically allows
-- configuration overrides via env vars or by using a custom Dockerfile to
-- mount an HBA file. For simplicity in a local test, the replication user
-- is often granted access via an included mechanism, but for full control,
-- you would need to ensure the following is in pg_hba.conf on the primary:
-- host replication replicator 0.0.0.0/0 scram-sha-256
