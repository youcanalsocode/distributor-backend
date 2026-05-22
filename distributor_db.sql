--
-- PostgreSQL database dump
--

\restrict nBqslyME7vkCUdkeSZxAGpmVvZSbAdhEviMjULNhnIChbzUI3HzCjsHDbbmc4UO

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: admins; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admins (
    id integer NOT NULL,
    mobile character varying NOT NULL,
    name character varying NOT NULL,
    password_hash character varying NOT NULL,
    security_question character varying,
    security_answer character varying
);


ALTER TABLE public.admins OWNER TO postgres;

--
-- Name: admins_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.admins_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.admins_id_seq OWNER TO postgres;

--
-- Name: admins_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.admins_id_seq OWNED BY public.admins.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying,
    image_url character varying
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: order_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_items (
    id integer NOT NULL,
    order_id integer,
    product_id integer,
    quantity integer,
    price double precision
);


ALTER TABLE public.order_items OWNER TO postgres;

--
-- Name: order_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.order_items_id_seq OWNER TO postgres;

--
-- Name: order_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_items_id_seq OWNED BY public.order_items.id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    restaurant_id integer,
    total_amount double precision,
    status character varying,
    created_at timestamp without time zone
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.orders_id_seq OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    category_id integer,
    name character varying NOT NULL,
    description character varying,
    price double precision,
    stock integer,
    unit character varying,
    image_url character varying
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: restaurants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.restaurants (
    id integer NOT NULL,
    mobile character varying NOT NULL,
    name character varying NOT NULL,
    address character varying,
    password_hash character varying NOT NULL,
    security_question character varying,
    security_answer character varying
);


ALTER TABLE public.restaurants OWNER TO postgres;

--
-- Name: restaurants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.restaurants_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.restaurants_id_seq OWNER TO postgres;

--
-- Name: restaurants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.restaurants_id_seq OWNED BY public.restaurants.id;


--
-- Name: admins id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admins ALTER COLUMN id SET DEFAULT nextval('public.admins_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: order_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items ALTER COLUMN id SET DEFAULT nextval('public.order_items_id_seq'::regclass);


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: restaurants id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.restaurants ALTER COLUMN id SET DEFAULT nextval('public.restaurants_id_seq'::regclass);


--
-- Data for Name: admins; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.admins VALUES (1, '9999999999', 'vimekrestomart', '$2b$12$ymHKYC8ZnAMaHG1.vyDWxe9nRqLMA13swsoNg2VUgEjuo1Bmsxn5a', 'What is your favorite food?', 'pizza');


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categories VALUES (2, 'Garlic', 'Garlic', NULL);
INSERT INTO public.categories VALUES (3, 'Paneer', 'Paneer', NULL);
INSERT INTO public.categories VALUES (4, 'Green Peas', 'Fresh green peas, naturally sweet and tender, ideal for bulk purchase, cooking, freezing, and resale.', NULL);
INSERT INTO public.categories VALUES (5, 'SweetCorn', 'Fresh sweet corn kernels, naturally juicy and sweet, perfect for bulk purchase, cooking, snacking, and resale.', NULL);
INSERT INTO public.categories VALUES (6, 'Mava', 'Fresh mava, rich and creamy dairy product, ideal for sweets, desserts, bulk purchase, and resale.', NULL);
INSERT INTO public.categories VALUES (7, 'Cheese', 'Fresh cheese, rich, creamy, and flavorful dairy product, ideal for cooking, baking, snacking, bulk purchase, and resale across businesses.', NULL);


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.order_items VALUES (1, 1, 4, 3, 230);
INSERT INTO public.order_items VALUES (2, 2, 4, 3, 230);
INSERT INTO public.order_items VALUES (3, 2, 5, 3, 260);
INSERT INTO public.order_items VALUES (4, 2, 7, 3, 80);
INSERT INTO public.order_items VALUES (5, 3, 4, 3, 230);
INSERT INTO public.order_items VALUES (6, 4, 4, 1, 230);
INSERT INTO public.order_items VALUES (7, 4, 5, 1, 260);
INSERT INTO public.order_items VALUES (8, 4, 7, 1, 80);
INSERT INTO public.order_items VALUES (9, 4, 2, 3, 110);
INSERT INTO public.order_items VALUES (10, 5, 10, 4, 310);
INSERT INTO public.order_items VALUES (11, 5, 2, 5, 110);
INSERT INTO public.order_items VALUES (12, 5, 7, 3, 80);
INSERT INTO public.order_items VALUES (13, 1, 4, 1, 230);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.orders VALUES (1, 3, 230, 'delivered', '2026-05-07 14:16:19.302625');


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.products VALUES (4, 3, ' Salted Paneer', 'Get your fresh  Salted paneer with high quality', 230, 20, '1Kg', '/uploads/790f24df-7442-4648-94c1-701785c149ff.jpg');
INSERT INTO public.products VALUES (5, 3, ' Malai Paneer', 'Get your fresh  Malai paneer with high quality', 260, 20, '1Kg', '/uploads/221fc4f0-b739-4d08-abc9-61622a83eed8.jpg');
INSERT INTO public.products VALUES (7, 4, 'Loose Green Peas', 'Fresh loose green peas, naturally sweet and tender, perfect for bulk buying, cooking, freezing, and resale.', 80, 35, '1Kg', '/uploads/5cfde794-7e01-4e05-a32b-44fc3f9467cf.jpg');
INSERT INTO public.products VALUES (2, 2, 'Garlic Peeled', 'Get your fresh peeled garlic with high quality', 110, 25, '1Kg', '/uploads/e67f615b-9d69-4ea4-990c-3a0bbbb502d4.jpg');
INSERT INTO public.products VALUES (8, 5, 'SweetCorn', 'Fresh sweet corn kernels, naturally juicy and sweet, perfect for bulk purchase, cooking, snacking, and resale.', 70, 10, '1kg', '/uploads/389f72ec-7841-415d-84cf-5179ed761833.jpg');
INSERT INTO public.products VALUES (9, 6, 'Mawa', 'Fresh mava, rich and creamy dairy product, ideal for sweets, desserts, bulk purchase, and resale.', 280, 20, '1Kg', '/uploads/78f99d52-71d6-42a3-8003-51171e47100e.jpg');
INSERT INTO public.products VALUES (10, 7, 'Milky Block cheese', 'Milky block cheese, rich, creamy texture with smooth flavor, perfect for slicing, cooking, melting, bulk purchase, and resale.', 310, 10, '1Kg', '/uploads/ffc52939-15e8-4306-91d2-bd6ae74b95d8.jpg');
INSERT INTO public.products VALUES (11, 7, 'Enjoy Cheese', 'Enjoy cheese, rich and creamy dairy delight, perfect for cooking, snacking, melting, and bulk purchase for resale businesses.', 300, 20, '1Kg', '/uploads/6f5b3ab5-f752-45e5-bf99-ebce59a02d0e.jpg');


--
-- Data for Name: restaurants; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.restaurants VALUES (3, '8888888888', 'Neha Italian Corner', 'Byculla(w) Station Road Kasim Manzil, Shop-10 , Mumbai-11', '$2b$12$uGALuFF2A8mGSlz7o6LZ/OQTWQ4CcV.9GYguwrsbaYeSOuNWsple2', 'What is your favorite food?', 'pizza');


--
-- Name: admins_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.admins_id_seq', 1, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 7, true);


--
-- Name: order_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_items_id_seq', 13, true);


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 1, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 11, true);


--
-- Name: restaurants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.restaurants_id_seq', 3, true);


--
-- Name: admins admins_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admins
    ADD CONSTRAINT admins_pkey PRIMARY KEY (id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: restaurants restaurants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.restaurants
    ADD CONSTRAINT restaurants_pkey PRIMARY KEY (id);


--
-- Name: ix_admins_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_admins_id ON public.admins USING btree (id);


--
-- Name: ix_admins_mobile; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_admins_mobile ON public.admins USING btree (mobile);


--
-- Name: ix_categories_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_categories_id ON public.categories USING btree (id);


--
-- Name: ix_order_items_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_order_items_id ON public.order_items USING btree (id);


--
-- Name: ix_orders_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_orders_id ON public.orders USING btree (id);


--
-- Name: ix_products_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_products_id ON public.products USING btree (id);


--
-- Name: ix_restaurants_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_restaurants_id ON public.restaurants USING btree (id);


--
-- Name: ix_restaurants_mobile; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_restaurants_mobile ON public.restaurants USING btree (mobile);


--
-- Name: order_items order_items_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: orders orders_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(id);


--
-- Name: products products_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- PostgreSQL database dump complete
--

\unrestrict nBqslyME7vkCUdkeSZxAGpmVvZSbAdhEviMjULNhnIChbzUI3HzCjsHDbbmc4UO

