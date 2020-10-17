USE course_vila;

CREATE TABLE `cv_course_group` (
	`id` INT(10) NOT NULL AUTO_INCREMENT COMMENT 'unique id of course group',
	`name` VARCHAR(255) NOT NULL DEFAULT "<Not Provided>" COMMENT 'name of course group',
	`description` VARCHAR(1000) COMMENT 'description of course group',
	`search_keywords` VARCHAR(1000) NOT NULL DEFAULT "<Not Provided>" COMMENT 'keywords used to search this course group',
	`associated_course_groups` VARCHAR(255) COMMENT 'other course groups associated with this group',
	`associated_course_ids` VARCHAR(255) COMMENT 'associated courses with this course group. this is a recursive dependency',
	PRIMARY KEY (`id`)
);

CREATE TABLE `cv_tutor_info` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL DEFAULT "<Not Provided>" COMMENT 'name of the tutor',
	`fb_profile` VARCHAR(255) COMMENT 'FB profile url if any',
	`twitter_handle` VARCHAR(255) COMMENT 'Twitter handle if any',
	`linkedin_profile` VARCHAR(255) COMMENT 'LinkedIn profile url if any',
	`git_profile` VARCHAR(255) COMMENT 'GIT profile url if any',
	`sof_profile` VARCHAR(255) COMMENT 'StackOverFlow profile url if any',
	`experience_month` INT(10) COMMENT 'experience in months',
	`background_info` VARCHAR(1000) COMMENT 'other info',
	PRIMARY KEY (`id`)
);
select * from cv_tutor_info;
insert into cv_tutor_info(name) value('Arpit');
CREATE TABLE `cv_course` (
	`id` INT(10) NOT NULL AUTO_INCREMENT COMMENT 'course id',
	`course_group_id` INT(10) NOT NULL DEFAULT 1 COMMENT 'course group id',
	`name` VARCHAR(255) NOT NULL DEFAULT "<Not Provided>" COMMENT 'name of the course',
	`search_keywords` VARCHAR(1000) COMMENT 'keywords to search this course. this is different from course group keyword search',
	`description` VARCHAR(1000) COMMENT 'description of the course',
	`course_provider` VARCHAR(255) COMMENT 'website providing course',
	`course_url` VARCHAR(1000) COMMENT 'open url of the course',
	`tutor_id` INT(10) NOT NULL DEFAULT 1 COMMENT 'Id of the tutor',
	`rating` FLOAT(10) COMMENT 'average rating out of 5',
	`rating_count` INT(10) COMMENT 'number of students who provided ratings',
	`student_count` INT(10) COMMENT 'number of students enrolled',
	`last_updated` DATE COMMENT 'date on course updated by tutor/owner',
	`supported_lang` VARCHAR(255) COMMENT 'course support on languaues',
	`price` INT(10) NOT NULL DEFAULT 0 COMMENT 'course cost',
	`course_content_id` INT(10) COMMENT 'course content id',
	`accessibility` VARCHAR(255) COMMENT 'access time of course for student e.g. lifetime',
	`devices` VARCHAR(255) COMMENT 'devices supported',
	`certification` BOOLEAN COMMENT 'certification is provided or not',
	`created_on` DATE NOT NULL COMMENT 'course inserted on db',
	`updated_on` DATE NOT NULL COMMENT 'course updated on db',
	PRIMARY KEY (`id`,`course_group_id`),
	FOREIGN KEY (`course_group_id`) REFERENCES `cv_course_group`(`id`),
	FOREIGN KEY (`tutor_id`) REFERENCES `cv_tutor_info`(`id`)
);

CREATE TABLE `cv_course_content` (
	`id` INT(10) NOT NULL AUTO_INCREMENT COMMENT 'course content id',
	`course_id` INT(10) NOT NULL DEFAULT 0 COMMENT 'course id for content',
	`duration` FLOAT(10) NOT NULL DEFAULT 0.0 COMMENT 'duration in hours',
	`resource_count` INT(10) COMMENT 'number of resources pdf, weblinks etc',
	`lecture_count` INT(10) COMMENT 'number of lectures in course',
	`section_count` INT(10) COMMENT 'number of sections in course',
	PRIMARY KEY (`id`),
	FOREIGN KEY (`course_id`) REFERENCES `cv_course`(`id`)
);

INSERT INTO `cv_course_group` (`id`, `name`, `description`, `search_keywords`, `associated_course_groups`, `associated_course_ids`) VALUES ('1', 'NODEJS', 'Course NODEJS', 'nodejs', NULL, NULL), ('2', 'REACT', 'Courses for react js', 'react,reactjs,react-native,react-core', NULL, NULL);





