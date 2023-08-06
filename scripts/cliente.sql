CREATE TABLE "public"."clientes"(
   "id" serial PRIMARY KEY,
   "nome" character varying(100) NOT NULL,
   "cpf" character varying(14) NOT NULL,
   "rg" character varying(20) NOT NULL,
   "data_nascimento" date NOT NULL,
   "cep" character varying(10) NOT NULL,
   "numero_residencia" character varying(5) NOT NULL,
   "logradouro" character varying(50) NOT NULL,
   "complemento" character varying(20),
   "bairro" character varying(30) NOT NULL,
   "cidade" character varying(30) NOT NULL,
   "estado" character varying(2) NOT NULL
);