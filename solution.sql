drop table if exists people;
drop table if exists places;

CREATE TABLE `places` (
	`id` int not null auto_increment,
    `city` varchar(80) default null,
    `county` varchar(80) default null,
    `country` varchar(80) default null,
    primary key (`id`)
    );
CREATE TABLE `people` (
  `id` int not null auto_increment,
  `given_name` varchar(80) default null,
  `family_name` varchar(80) default null,
  `place_of_birth` varchar(80) default null,
  `date_of_birth` date not null,
  `city_id` int default null,
  primary key (`id`),
  CONSTRAINT FK_PeoplePlaces
  FOREIGN KEY (city_id) REFERENCES places(id)
);
