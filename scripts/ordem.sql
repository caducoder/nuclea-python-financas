CREATE TABLE "public"."ordens"(
   "id" serial PRIMARY KEY,
   "nome" character varying(100) NOT NULL,
   "ticket" character varying(10) NOT NULL,
   "valor_compra" numeric NOT NULL,
   "quantidade_compra" numeric NOT NULL,
   "data_compra" date NOT NULL,
   "cliente_id" integer NOT NULL,
   constraint fk_cliente foreign key (cliente_id) references clientes(id)
);