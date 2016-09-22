#!/usr/bin/env bash

sudo su - postgres & psql

CREATE DATABASE mysite;
CREATE USER kevin WITH PASSWORD '10100813';

ALTER ROLE kevin SET client_encoding TO 'utf8';
ALTER ROLE kevin SET default_transaction_isolation TO 'read committed';
#ALTER ROLE kevin SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE mysite TO kevin;
