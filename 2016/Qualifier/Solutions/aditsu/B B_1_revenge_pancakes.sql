-- This code is written for PostgreSQL 9.4+

-- Run it like this:
-- psql -qAtf B_1_revenge_pancakes.sql dbname username < inputfile

-- You can create a new database for running the code,
-- or you can use an existing database

CREATE temp TABLE pancakes (
  id serial NOT NULL primary key,
  line varchar
);

\copy pancakes(line) from pstdin

select 'Case #' || (id - 1) || ': ' || (array_length(regexp_split_to_array(line, '\+-'), 1)
 + array_length(regexp_split_to_array(line, '-\+'), 1) - 1 - (right(line, 1) = '+') :: int)
from pancakes where id > 1 order by id;
