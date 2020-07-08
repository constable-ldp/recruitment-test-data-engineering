### Completed task - Luke Constable

Added python script and sql, and updated docker and requirement files. 

To run use the commands below: 

docker-compose up database

docker-compose build

docker-compose run database mysql --host=database --user=codetest --password=swordfish codetest < solution.sql

docker-compose run solution

docker-compose down
