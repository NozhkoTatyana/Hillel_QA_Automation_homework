--
-- PostgreSQL database dump
--

\restrict kyAZVg6RGtzW1ISUwJqHf8lunFYDofXH5bdNQAkNAKM5HZHI2nV7H5Pk9UKkwy1

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.3

-- Started on 2026-06-28 19:34:48

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16620)
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    title character varying(100) NOT NULL
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16619)
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.courses_id_seq OWNER TO postgres;

--
-- TOC entry 5034 (class 0 OID 0)
-- Dependencies: 221
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- TOC entry 223 (class 1259 OID 16628)
-- Name: enrollments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enrollments (
    student_id integer NOT NULL,
    course_id integer NOT NULL
);


ALTER TABLE public.enrollments OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16608)
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL
);


ALTER TABLE public.students OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16607)
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.students_id_seq OWNER TO postgres;

--
-- TOC entry 5035 (class 0 OID 0)
-- Dependencies: 219
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- TOC entry 4866 (class 2604 OID 16623)
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- TOC entry 4865 (class 2604 OID 16611)
-- Name: students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- TOC entry 5027 (class 0 OID 16620)
-- Dependencies: 222
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (id, title) FROM stdin;
3	Computer Science
4	History
5	Literature
2	new_course
\.


--
-- TOC entry 5028 (class 0 OID 16628)
-- Dependencies: 223
-- Data for Name: enrollments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enrollments (student_id, course_id) FROM stdin;
1	5
2	3
3	3
3	2
4	4
4	3
6	2
7	5
7	2
7	4
8	2
9	3
9	4
10	2
11	3
11	5
12	3
12	2
13	5
13	4
14	2
15	4
16	5
17	5
17	4
18	3
18	5
\.


--
-- TOC entry 5025 (class 0 OID 16608)
-- Dependencies: 220
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (id, name, email) FROM stdin;
1	Steven Rice	tmoore@example.com
2	Crystal Gill	coxkevin@example.org
3	Lisa Matthews	eibarra@example.net
4	Shane Fletcher	michael27@example.net
6	Tamara Anthony	christopher87@example.com
7	Amanda Vincent	michaelkaiser@example.net
8	Eric Davidson	scottjamie@example.com
9	Christopher Castillo	kimberlynelson@example.com
10	Edwin Kerr	chavezdawn@example.org
11	Emily Carr	ritterjuan@example.net
12	Aaron Brown	amanda53@example.org
13	Dr. Travis Booth	candace09@example.org
14	Ryan West	bakersharon@example.net
15	Tiffany Alexander	cabreravictoria@example.net
16	Richard Poole	matthewmartinez@example.org
17	Juan Gross	jonathan80@example.com
18	Austin Moore	grayjoshua@example.org
19	Alexis Robinson	taylorthomas@example.org
\.


--
-- TOC entry 5036 (class 0 OID 0)
-- Dependencies: 221
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_id_seq', 5, true);


--
-- TOC entry 5037 (class 0 OID 0)
-- Dependencies: 219
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 23, true);


--
-- TOC entry 4872 (class 2606 OID 16627)
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- TOC entry 4874 (class 2606 OID 16634)
-- Name: enrollments enrollments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments
    ADD CONSTRAINT enrollments_pkey PRIMARY KEY (student_id, course_id);


--
-- TOC entry 4868 (class 2606 OID 16618)
-- Name: students students_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_email_key UNIQUE (email);


--
-- TOC entry 4870 (class 2606 OID 16616)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- TOC entry 4875 (class 2606 OID 16640)
-- Name: enrollments enrollments_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments
    ADD CONSTRAINT enrollments_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(id) ON DELETE CASCADE;


--
-- TOC entry 4876 (class 2606 OID 16635)
-- Name: enrollments enrollments_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollments
    ADD CONSTRAINT enrollments_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(id) ON DELETE CASCADE;


-- Completed on 2026-06-28 19:34:48

--
-- PostgreSQL database dump complete
--

\unrestrict kyAZVg6RGtzW1ISUwJqHf8lunFYDofXH5bdNQAkNAKM5HZHI2nV7H5Pk9UKkwy1

