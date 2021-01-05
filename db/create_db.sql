drop database if exists statistics;
drop user if exists statistics;

create user statistics with encrypted password 'vanillasprite';
create database statistics;
grant all privileges on database statistics to statistics;
