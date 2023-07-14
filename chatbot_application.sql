-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 11, 2023 at 02:57 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatbot_application`
--

-- --------------------------------------------------------

--
-- Table structure for table `about_nstu`
--

CREATE TABLE `about_nstu` (
  `id` int(255) NOT NULL,
  `about` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `about_nstu`
--

INSERT INTO `about_nstu` (`id`, `about`) VALUES
(6, 'The creation of a band of skilled manpower equipped with latest knowledge of science and technology is a must to achieve a prestigious position in this modern world. As a part of ensuring quality education, with immense expectations of the southern coastal inhabitants of Bangladesh, a new university named Noakhali Science and Technology University (abbreviated as NSTU) was established on 15 July 2001 enacting the Noakhali Science and Technology University Act 2001. Finally, it started its academic activities on 22 June 2006. The inclusion of the study of humanities implies the urge felt by the concerned authority to create leaders who will fashion a more humane and just world. The university not only engages itself in teaching and research but also provides societal services for the benefit of rural and urban populations.\r\n\r\nAt present, it has six faculties (namely Faculty of Engineering & Technology, Faculty of Science, Faculty of social Science and humanities, Faculty of Business administration, faculty of education sciences and the faculty of Law) and two institutes (namely Institute of Information Science and Institute of Information Technology). The faculties include twenty-eight degree offering departments namely Department of Computer Science and Telecommunication Engineering (CSTE), Department of Fisheries & Marine Science (FIMS), Department of Pharmacy, Department of Applied Chemistry and Chemical Engineering (ACCE), Department of Microbiology, Department of Applied Mathematics, Department of English, Department of Environmental Science and Disaster Management (ESDM), Department of Food Technology and Nutrition Science (FTNS), Department of Business Administration, Department of Information and Communication Engineering (ICE), Department of Economics, Department of Biotechnology and Genetic Engineering (BGE),Department of Bangla,Department of Biochemistry and Molecular Biology, Department of Agriculture (AG), Department of Statistics, Department of Electrical and Electronic Engineering (EEE),Department of Zoology, Department of Law, Department of Education, Department of Education Administration, Department of Sociology, Department of tourism and Hospitality management, Department of Management Information Systems,  Department of Social Administration, Department of Bangladesh and Liberation War Studies and Department of Oceanography.\r\nThe well-furnished central library equipped with online library facilities has 10,000 printed books and 1500 printed journals apart from numerous e-books and e-journals. Since its establishment, NSTU has been running very smoothly. The teachers have extraordinary academic background and excellent skill of presentation. Presently, one fourth of the teachers are doing PhD in different parts of the world. This is the only university in Bangladesh where three individual subjects based exclusively on information study namely Information Science, Information Technology, and Information and Communication Engineering is taught. International conferences, seminars and symposiums are frequently held with participation of the scholars from all over the world. Internal Programming contest is arranged regularly to sharpen the skill as a result of which many national and international awards in programming contests are already in the store of this university. Students of Fisheries and Marine Science as well as Oceanography with their extensive research on healthy marine resources privileged by the location of this university in a coastal arena are contributing greatly to the country’s blue economy.\r\n\r\nCo-curricular activities are extensively patronized. There are students’ organizations like NSTUMUNA, NSTU Debating Society, and NSTU English Club, NSTU Business Club etc. which work to develop leadership capacity of a student by promoting the art of public speaking, reasoning and logical thinking. Besides, NSTU Blood Donors Society, DreamBazz Filmz, Moshal, Protiddhoni, NSTU Photographic Society etc are there whose activities aim at the formation of a non-communal and progressive cultural mind. The way the national and international days are observed and different cultural festivals are celebrated with active participation of not only the students but the local dwellers as well has turned the campus into a cultural capital of this southern region. The slogan “Green NSTU, Clean NSTU” has been an inspiring tonic among all in keeping this naturally blessed green campus neat and clean. The calm, quiet & soothing environment of the campus, modeled upon the western modern universities like the University of Cambridge, is a wonderful escape for the researchers from the hustle and bustle of town life for an uninterrupted concentration on their study and research. Now-a-days, NSTU is lovingly addressed as The Cambridge of the Coastal Terrain. Each member of NSTU family is trying hard to make this addressing a reality.');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_picture` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`, `profile_picture`) VALUES
(1, 'Admin', 'admin@gmail.com', 'admin', 'Admin.png');

-- --------------------------------------------------------

--
-- Table structure for table `chancellor_corner`
--

CREATE TABLE `chancellor_corner` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `speech` longtext NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chancellor_corner`
--

INSERT INTO `chancellor_corner` (`id`, `name`, `speech`, `image`) VALUES
(3, 'Mr President', 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is availablIn publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is availablIn publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is availablIn publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is availablIn publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is availabl', 'Mr President.jpg'),
(4, 'Mohammed Shahabuddin', 'Mr. Mohammed Shahabuddin was born on December 10, 1949 in Jubilee Tank Para of Shibrampur, Pabna city. His father\'s name is Sharfuddin Ansari, mother\'s name is Khairunnessa.\r\n\r\nMr. Mohammed Shahabuddin passed SSC in 1966 from Radhanagar Majumdar Academy, HSC in 1968 from Pabna Edward College and obtained BSc degree in 1971 (held in 1972). Later he received his Masters in Psychology from Rajshahi University in 1974. In 1975 he did his LLB from Pabna Shaheed Aminuddin Law College and out of 103 candidates only he passed and obtained Higher Second Class in that examination. \r\n\r\nHe was involved in politics during his student life. He served as the General Secretary of Pabna Edward College Chhatra League in 1967-68, Vice-President of Undivided Pabna District Chhatra League in 1969-70 and President of Pabna District Chhatra League in 1970-73. Mr. Mohammed Shahabuddin was one of the flag hoisters of Bangladesh at the Pabna Town Hall Maidan on March 23, 1971. He served as the convener of Pabna District Shadhin Bangla Chatra Sangram Parishad.\r\n\r\nMr. Mohammed Shahabuddin actively participated in the great Liberation War in 1971 as a member of ‘Mujib Bahini’.\r\n\r\nHe was President of Pabna District Jubo League in 1974. In 1975, when the Bangladesh Krishak-Sramik-Awami League (BAKSAL) was formed, Father of the Nation Bangabandhu Sheikh Mujibur Rahman nominated him as the joint secretary of Pabna District BAKSAL.\r\n\r\nMr. Mohammed Shahabuddin led a procession in Pabna protesting the brutal assassination of Father of the Nation Bangabandhu Sheikh Mujibur Rahman on August 15, 1975. Later he was arrested on August 20 and was tortured in an army camp for three months. He was sent to jail and was released in 1978 after three years of imprisonment. He was elected Publicity Secretary of Pabna District Awami League in 1980.\r\n\r\nMr. Mohammed Shahabuddin was a member of Pabna District Lawyers Association. He joined Bangladesh Civil Service (Judicial) Cadre in 1982. He was elected Secretary General of Bangladesh Judicial Service Association in 1995-1996. He stood first in both in-service training workshops for Additional District Judges and District Judges. He also served as the Chairman of the Labor Court. He was appointed by Ministry of Law as a coordinator for the Bangabandhu murder case.\r\n\r\nMohammed Shahabuddin retired as District and Sessions Judge in 2006 and returned to the law profession by joining the High Court Division of Bangladesh Supreme Court. He was the head of the investigation commission known as ‘Shahabuddin Commission’ formed for investigation of the incidents of attacks, murders, rapes and arson on the leaders and activists of Awami League and its allied organizations, and the people of the minority community during the BNP-Jamaat coalition government after the general election in 2001. The report of this commission was published in the official gazette.\r\n\r\nMohammed Shahabuddin served as Commissioner of Anti-Corruption Commission (ACC) from 2011 to 2016. At that time, the World Bank brought charges of corruption in the Padma Bridge construction project. Mr. Mohammed Shahabuddin played a strong role when the government assigned the ACC to investigate the matter and was able to disprove the World Bank\'s allegations. The Ontario Court of Justice of Toronto, Canada fully supported his investigation report while settling the case.\r\n\r\nMr. Mohammed Shahabuddin was elected as a member of Bangladesh Awami League Advisory Council in January 2020. He also served as the Chairman of the Publicity and Publication Sub-Committee of the Awami League\r\n\r\nMr. Shahabuddin served as President of Pabna Development Foundation. After independence, he was the General Secretary of Pabna District Red Crescent Society from 1972-1974 and the Treasurer of Pabna District Family Planning Society from 1973-1974. He is a life member of Pabna Press Club, Annada Govinda Public Library and Banamali Shilpacharcha Kendra.\r\n\r\nMr. Mohammed Shahabuddin\'s wife Dr. Rebeka Sultana retired as Joint Secretary to the Government in 2009. She is currently working as a professor and director of a private university. Md. Arshad Adnan is their only child. His twin grandsons Tahsin Md. Adnan and Tahmid Md. Adnan are studying in A-level.\r\n\r\nHis favorite hobbies are travelling, reading books and listening music.', 'Mohammed Shahabuddin.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `event_date` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`id`, `title`, `description`, `event_date`, `image`) VALUES
(4, 'IIT Project Showcase', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', '2023-07-19', 'IIT Project Showcase.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `feed_back`
--

CREATE TABLE `feed_back` (
  `id` int(255) NOT NULL,
  `feed_back_msg` varchar(255) NOT NULL,
  `feed_back_type` varchar(255) NOT NULL,
  `user_text` varchar(255) NOT NULL,
  `bot_response` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`id`, `title`, `file`, `time`) VALUES
(4, 'Latest Job', 'Latest Job.pdf', '2023-07-01 14:48:12');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `title`, `description`, `image`, `time`) VALUES
(6, 'IIT First Batch Farewell', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 'IIT First Batch Farewell.jpg', '2023-07-05 00:19:05');

-- --------------------------------------------------------

--
-- Table structure for table `new_query_data`
--

CREATE TABLE `new_query_data` (
  `id` int(255) NOT NULL,
  `feed_back_id` varchar(255) NOT NULL,
  `tag` varchar(255) NOT NULL,
  `patterns` varchar(255) NOT NULL,
  `responses` varchar(255) NOT NULL,
  `context` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notices`
--

CREATE TABLE `notices` (
  `id` int(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `upload_time` datetime(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notices`
--

INSERT INTO `notices` (`id`, `title`, `file_name`, `image`, `upload_time`) VALUES
(5, 'Notice 1', 'Notice 1.pdf', 'Notice 1.jpg', '2023-07-01 14:23:21.849566');

-- --------------------------------------------------------

--
-- Table structure for table `provc_corner`
--

CREATE TABLE `provc_corner` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `speech` longtext NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `provc_corner`
--

INSERT INTO `provc_corner` (`id`, `name`, `speech`, `image`) VALUES
(3, 'Abdul Baki', 'Professor Dr. Mohammad Abdul Baki has been appointed as the new Pro-Vice Chancellor of Noakhali Science and Technology University (NSTU).He is a professor in the Department of Zoology, Jagannath University. His Excellency President and Chancellor of the University Mr. Md. Abdul Hamid has given this appointment for the next four years as per Section 12(1) of NSTU Act 2001.On Wednesday, 25 August 2021, with the approval of His Excellency the President and the Chancellor, the Secondary and Higher Education Department of the Ministry of Education issued a notification in this regard. This order will be implemented immediately.\r\n\r\nProfessor Dr. Mohammad Abdul Baki has been appointed as the new Pro-Vice Chancellor of Noakhali Science and Technology University (NSTU).He is a professor in the Department of Zoology, Jagannath University. His Excellency President and Chancellor of the University Mr. Md. Abdul Hamid has given this appointment for the next four years as per Section 12(1) of NSTU Act 2001.On Wednesday, 25 August 2021, with the approval of His Excellency the President and the Chancellor, the Secondary and Higher Education Department of the Ministry of Education issued a notification in this regard. This order will be implemented immediately.\r\nProfessor Dr. Mohammad Abdul Baki has been appointed as the new Pro-Vice Chancellor of Noakhali Science and Technology University (NSTU).He is a professor in the Department of Zoology, Jagannath University. His Excellency President and Chancellor of the University Mr. Md. Abdul Hamid has given this appointment for the next four years as per Section 12(1) of NSTU Act 2001.On Wednesday, 25 August 2021, with the approval of His Excellency the President and the Chancellor, the Secondary and Higher Education Department of the Ministry of Education issued a notification in this regard. This order will be implemented immediately.\r\n', 'Abdul Baki.jpg'),
(4, 'Professor Dr. Mohammad Abdul Baki', 'Professor Dr. Mohammad Abdul Baki has been appointed as the new Pro-Vice Chancellor of Noakhali Science and Technology University (NSTU).He is a professor in the Department of Zoology, Jagannath University. His Excellency President and Chancellor of the University Mr. Md. Abdul Hamid has given this appointment for the next four years as per Section 12(1) of NSTU Act 2001.On Wednesday, 25 August 2021, with the approval of His Excellency the President and the Chancellor, the Secondary and Higher Education Department of the Ministry of Education issued a notification in this regard. This order will be implemented immediately.', 'Professor Dr. Mohammad Abdul Baki.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `queries`
--

CREATE TABLE `queries` (
  `id` int(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `user_text` varchar(255) NOT NULL,
  `chatbot_response` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `register_corner`
--

CREATE TABLE `register_corner` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `speech` longtext NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register_corner`
--

INSERT INTO `register_corner` (`id`, `name`, `speech`, `image`) VALUES
(2, 'Mr Register', 'The Registrar Office at NSTU is committed to lay its best effort at every field/department and discharge privileges to its stakeholders. The task of the Registrar office is to provide support to every student with enrollment/registration, course information and keep the student\'s records to dispense degree clearance and certification in congruence with the existing university statute. Moreover, the office takes care of every necessity to ensure quality education by employing competent faculties for academic purposes and administrative staff of various offices. Furthermore, the office facilitates multiple sections such as education section, council section, establishment section, administrative section, estate & housing section, security section, central store section and despatch section where stakeholders come to the directives for varsity needs and the regulation for executing differe The Registrar Office at NSTU is committed to lay its best effort at every field/department and discharge privileges to its stakeholders. The task of the Registrar office is to provide support to every student with enrollment/registration, course information and keep the student\'s records to dispense degree clearance and certification in congruence with the existing university statute. Moreover, the office takes care of every necessity to ensure quality education by employing competent faculties for academic purposes and administrative staff of various offices. Furthermore, the office facilitates multiple sections such as education section, council section, establishment section, administrative section, estate & housing section, security section, central store section and despatch section where stakeholders come to the directives for varsity needs and the regulation for executing differe The Registrar Office at NSTU is committed to lay its best effort at every field/department and discharge privileges to its stakeholders. The task of the Registrar office is to provide support to every student with enrollment/registration, course information and keep the student\'s records to dispense degree clearance and certification in congruence with the existing university statute. Moreover, the office takes care of every necessity to ensure quality education by employing competent faculties for academic purposes and administrative staff of various offices. Furthermore, the office facilitates multiple sections such as education section, council section, establishment section, administrative section, estate & housing section, security section, central store section and despatch section where stakeholders come to the directives for varsity needs and the regulation for executing differe The Registrar Office at NSTU is committed to lay its best effort at every field/department and discharge privileges to its stakeholders. The task of the Registrar office is to provide support to every student with enrollment/registration, course information and keep the student\'s records to dispense degree clearance and certification in congruence with the existing university statute. Moreover, the office takes care of every necessity to ensure quality education by employing competent faculties for academic purposes and administrative staff of various offices. Furthermore, the office facilitates multiple sections such as education section, council section, establishment section, administrative section, estate & housing section, security section, central store section and despatch section where stakeholders come to the directives for varsity needs and the regulation for executing differe', 'Mr Register.jpg'),
(3, 'Dr Newaz Mohammad bahadur', 'Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.', 'Dr Newaz Mohammad bahadur.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `research`
--

CREATE TABLE `research` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `journal_url` varchar(255) NOT NULL,
  `publication_date` varchar(255) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `research`
--

INSERT INTO `research` (`id`, `title`, `author`, `journal_url`, `publication_date`, `description`) VALUES
(3, 'NSTU IIT Research', 'Tasniya Ahmed', 'https://www.linkedin.com.bd/', '2023-07-04', 'The Registrar Office at NSTU is committed to lay its best effort at every field/department and discharge privileges to its stakeholders. The task of the Registrar office is to provide support to every student with enrollment/registration, course information and keep the student\'s records to dispense degree clearance and certification in congruence with the existing university statute.');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `student_id` varchar(255) NOT NULL,
  `designation` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `session` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `about` longtext NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `linkedin` varchar(255) NOT NULL,
  `facebook` varchar(255) NOT NULL,
  `twitter` varchar(255) NOT NULL,
  `degree` longtext NOT NULL,
  `journal` longtext NOT NULL,
  `research_interest` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `student_id`, `designation`, `department`, `session`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter`, `degree`, `journal`, `research_interest`, `password`) VALUES
(1, 'Md Al Adnan', 'ASH1825008M', 'undergraduate', 'iit', '2018-2017', 'Md Al Adnan.jpg', 'First batch student', 'adnan2513@nstu.edu.bd', '01406980019', 'https://www.linkedin.com/aladnansami', 'https://www.facebook.com/al.adnan.18', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', '[[\"BS In Software Engineering\", \"Noakhali Science And Technology University\", \"First batch student\", \"2023\"]]', '[[\"\", \"\", \"\", \"\", \"\"]]', 'Mechine Learning', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `designation` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `about` longtext NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `linkedin` varchar(255) NOT NULL,
  `facebook` varchar(255) NOT NULL,
  `twitter` varchar(255) NOT NULL,
  `degree` longtext NOT NULL,
  `journal` longtext NOT NULL,
  `password` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`id`, `name`, `designation`, `department`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter`, `degree`, `journal`, `password`) VALUES
(14, 'Dr. Mohammad Salim Hossain', 'professor', 'iit', 'Dr. Mohammad Salim Hossain.jpg', 'To be provided soon....', 'salim@gmail.com', '01406980019', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', '[[\"M.Sc. In Software Engineering\", \"Institute of Information Technology, University of Dhaka, Bangladesh\", \"To be provided soon....\", \"2011\"]]', '[[\"Trend Estimation Of Stock Market: An Intelligent Decision System\", \"Mohammad Ibrahim, Md. Iftekharul Alam Efat, Tajkia Rahman Toma, Shah Mostafa Khaled, Md. Shariful Islam, Mohammad Shoyaib\", \"Cyber Security\", \"https://www.linkedin.com/pub/dir/Aditya/Ravikumar\", \"2023-07-11\"]]', '1234'),
(16, 'Md. Nuruzzaman Bhuiyan', 'assistantprofessor', 'iit', 'Md. Nuruzzaman Bhuiyan.jpg', 'Provided to be soon....', 'nuruzzaman.iit@nstu.edu.bd', '8801612032781', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', '[[\"M.Sc. In Software Engineering\", \"Institute of Information Technology, University of Dhaka, Bangladesh\", \"Provided to be soon....\", \"2010\"]]', '[[\"Lorem Ipsum is simply dummy text of the printing and typesetting industry.\", \"Mohammad Ibrahim, Md. Nuruzzaman Bhuiyan, Tajkia Rahman Toma, Shah Mostafa Khaled, Md. Shariful Islam, Mohammad Shoyaib\", \"Dynamic Blocks For Face Verification\", \"https://www.linkedin.com/pub/dir/Aditya/Ravikumar\", \"2023-07-06\"]]', '1234'),
(17, 'Md. Auhidur Rahaman', 'assistantprofessor', 'iit', 'Md. Auhidur Rahaman.jpg', 'Provided to be soon....', 'auhidsumon@nstu.edu.bd', '8801815662160', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', 'https://www.linkedin.com/pub/dir/Aditya/Ravikumar', '[[\"M.Sc. In CSTE\", \"Noakhali Science And Technology University\", \"Provided to be soon....\", \"2010\"]]', '[[\"Lorem Ipsum is simply dummy text of the printing and typesetting industry.\", \"Mohammad Ibrahim, Md. Auhidur Rahaman, Tajkia Rahman Toma, Shah Mostafa Khaled, Md. Shariful Islam, Mohammad Shoyaib\", \"Cyber Security\", \"https://www.linkedin.com/pub/dir/Aditya/Ravikumar\", \"2023-07-05\"]]', '1234'),
(19, 'Tasniya Ahmed', 'assistantprofessor', 'iit', 'Tasniya Ahmed.jpg', 'Provided to be soon....', 'tasniya.iit@nstu.edu.bd', '01936543596', 'https://www.linkedin.com/in/tasniya-ahmed-9a0a891a5/', 'https://www.facebook.com/tasniya.neela', 'https://www.twitter.com/', '[[\" Computer Science & Engineering (CSE)\", \"Jahangirnagar University\", \"Provided to be soon....\", \"2012\"]]', '[[\"Provided to be soon....\", \"Tasniya Ahmed\", \"Provided to be soon....\", \"https://www.linkedin.com/in/tasniya-ahmed-9a0a891a5/\", \"2023-07-10\"]]', '1234'),
(20, 'Md. Iftekharul Alam Efat', 'assistantprofessor', 'iit', 'Md. Iftekharul Alam Efat.jpg', 'An enthusiastic, adaptive and fast-learning person with a broad and acute interest in the field of Secure Software Design & Architecture. I particularly enjoycollaborating with Software Systems with Artificial Intelligence and solve new challenges.Currently, doing research on \"IoT Based Health Status Monitoring Technology\",using neural network that will be monitor health status of diabetics patients.', 'iftekhar.iit@nstu.edu.bd', '01727208714', 'https://www.linkedin.com/in/iftekhar-efat', 'https://www.facebook.com/uiftee', 'https://www.facebook.com/uiftee', '[[\"M.Sc. In Software Engineering\", \"Institute of Information Technology, University of Dhaka, Bangladesh\", \"Thesis: Reusability Measurement for Software Components\\r\\nCGPA \\u2013 3.79 (in the scale of 4.00)\", \"2010\"]]', '[[\"Dynamic Blocks For Face Verification\", \"Mohammad Ibrahim, Md. Iftekharul Alam Efat, Tajkia Rahman Toma, Shah Mostafa Khaled, Md. Shariful Islam, Mohammad Shoyaib\", \" International Journal of Computer Vision & Signal Processing (ISSN: 2186-0114)\", \"https://iitnstu.sererl.com/faculty_memberDetails.php\", \"2023-07-10\"]]', '1234'),
(21, 'Dipok Chandra Das', 'assistantprofessor', 'iit', 'Dipok Chandra Das.jpg', 'Provided to be soon....', 'dipok.iit@nstu.edu.bd', '01743972128', 'https://www.linkedin.com/in/dipok-chandra-das-06bb1711b/', 'https://www.facebook.com/cd.dipok', 'https://www.linkedin.com/in/dipok-chandra-das-06bb1711b/', '[[\"M.Sc. In Software Engineering\", \"Institute of Information Technology, University of Dhaka, Bangladesh\", \"Provided To be soon...\", \"2018\"]]', '[[\"Provider To be Soon...\", \"Dipok Chandra Das\", \"Provider To be Soon...\", \"https://www.linkedin.com/in/dipok-chandra-das-06bb1711b/\", \"2023-07-19\"]]', '1234'),
(22, 'Dipanita Saha', 'assistantprofessor', 'iit', 'Dipanita Saha.jpg', 'Provided to be soon...', 'dipanita.iit@nstu.edu.bd', '01534373338', 'https://www.facebook.com/dipanita.iit', 'https://www.facebook.com/dipanita.iit', 'https://www.facebook.com/dipanita.iit', '[[\" Master in computer science\", \"Jahangirnagar University\", \"Provided to be soon...\", \"2015\"]]', '[[\"Provided to be soon...\", \"Dipanita Saha\", \"Provided to be soon...\", \"https://www.facebook.com/dipanita.iit\", \"2023-07-10\"]]', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `treasurer_corner`
--

CREATE TABLE `treasurer_corner` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `speech` longtext NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `treasurer_corner`
--

INSERT INTO `treasurer_corner` (`id`, `name`, `speech`, `image`) VALUES
(2, 'Newaz Mohammed Bahadur', 'Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.', 'Newaz Mohammed Bahadur.jpg'),
(3, 'Dr. Newaz Mohammed Bahadur', 'Professor Dr. Newaz Mohammed Bahadur appointed as Treasurer of Noakhali Science and Technology University on 16 March 2023.He was appointed as the Treasurer by His Excellency the President of the People\'s Republic of Bangladesh and the Honorable Chancellor of the University as per the provisions of Section 13 (3) (4) (5) (6) and (7) of the Noakhali University of Science and Technology Act 2001. Professor Dr. Newaz Mohammed Bahadur is a renowned Professor of ACCE at Noakhali Science and Technology University (NSTU). He was elected former president of the university\'s teachers\' association several times. He also held important administrative duties including Regent board Member and Proctor of the University.', 'Dr. Newaz Mohammed Bahadur.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `fname`, `lname`, `email`, `pwd`) VALUES
(5, 'Md', 'Adnan', 'aladnansami21@gmail.com', '!87654321Aa');

-- --------------------------------------------------------

--
-- Table structure for table `vc_corner`
--

CREATE TABLE `vc_corner` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `speech` longtext NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vc_corner`
--

INSERT INTO `vc_corner` (`id`, `name`, `speech`, `image`) VALUES
(5, 'Md Billal Hossain', 'Hello guys, I\'m Md Billal Hossain.\r\n\r\nContrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.\r\n\r\nThe standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.\r\n\r\nContrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.\r\n\r\nThe standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.', 'Md Billal Hossain.jpg'),
(6, 'Professor Dr. Mohammad Abdul Baki', 'Professor Dr. Mohammad Abdul Baki has been appointed as the new Pro-Vice Chancellor of Noakhali Science and Technology University (NSTU).He is a professor in the Department of Zoology, Jagannath University. His Excellency President and Chancellor of the University Mr. Md. Abdul Hamid has given this appointment for the next four years as per Section 12(1) of NSTU Act 2001.On Wednesday, 25 August 2021, with the approval of His Excellency the President and the Chancellor, the Secondary and Higher Education Department of the Ministry of Education issued a notification in this regard. This order will be implemented immediately.', 'Professor Dr. Mohammad Abdul Baki.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `about_nstu`
--
ALTER TABLE `about_nstu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chancellor_corner`
--
ALTER TABLE `chancellor_corner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feed_back`
--
ALTER TABLE `feed_back`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `new_query_data`
--
ALTER TABLE `new_query_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notices`
--
ALTER TABLE `notices`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `provc_corner`
--
ALTER TABLE `provc_corner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queries`
--
ALTER TABLE `queries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register_corner`
--
ALTER TABLE `register_corner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `research`
--
ALTER TABLE `research`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `treasurer_corner`
--
ALTER TABLE `treasurer_corner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vc_corner`
--
ALTER TABLE `vc_corner`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `about_nstu`
--
ALTER TABLE `about_nstu`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `chancellor_corner`
--
ALTER TABLE `chancellor_corner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feed_back`
--
ALTER TABLE `feed_back`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `new_query_data`
--
ALTER TABLE `new_query_data`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `notices`
--
ALTER TABLE `notices`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `provc_corner`
--
ALTER TABLE `provc_corner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `queries`
--
ALTER TABLE `queries`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=224;

--
-- AUTO_INCREMENT for table `register_corner`
--
ALTER TABLE `register_corner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `research`
--
ALTER TABLE `research`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `treasurer_corner`
--
ALTER TABLE `treasurer_corner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vc_corner`
--
ALTER TABLE `vc_corner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
