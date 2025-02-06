-- Tämä on SQL-kielinen varmuuskopio testaus-tietokannasta
-- Luo ensin tietokanta PGAdmin ohjelmassa nimellä testaus
-- Avaa sen jälkeen kyselyikkuna (Query Editor) ja liitä 
-- tämä skripti ikkunaan ja paina suorita painiketta (kolmio)


-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.1

-- Started on 2025-01-15 11:03:31

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'WIN1252';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4850 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 19544)
-- Name: person; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.person (
    idnumero integer NOT NULL,
    etunimi character varying(30) NOT NULL,
    sukunimi character varying(30) NOT NULL
);


ALTER TABLE public.person OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 19543)
-- Name: person_idnumero_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.person_idnumero_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.person_idnumero_seq OWNER TO postgres;

--
-- TOC entry 4851 (class 0 OID 0)
-- Dependencies: 217
-- Name: person_idnumero_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.person_idnumero_seq OWNED BY public.person.idnumero;


--
-- TOC entry 4695 (class 2604 OID 19547)
-- Name: person idnumero; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.person ALTER COLUMN idnumero SET DEFAULT nextval('public.person_idnumero_seq'::regclass);


--
-- TOC entry 4844 (class 0 OID 19544)
-- Dependencies: 218
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.person VALUES (1, 'Ville', 'Virtanen');
INSERT INTO public.person VALUES (2, 'Jakke', 'J�yn�');
INSERT INTO public.person VALUES (3, 'Assi', 'Kalma');
INSERT INTO public.person VALUES (4, 'Tuittu', 'Kiukkunen');


--
-- TOC entry 4852 (class 0 OID 0)
-- Dependencies: 217
-- Name: person_idnumero_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.person_idnumero_seq', 4, true);


--
-- TOC entry 4697 (class 2606 OID 19549)
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (idnumero);


-- Completed on 2025-01-15 11:03:31

--
-- PostgreSQL database dump complete
--

