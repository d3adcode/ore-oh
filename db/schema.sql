create table statistics (
  id serial not null primary key,
  create_date timestamp with time zone not null default (current_timestamp at time zone 'utc'),
  source text not null,
  stat_id text not null,
  data json
);
