# Mexico: law history in git

The law of Mexico as a git history: one file per provision, one commit per decree on the day it took effect, and the decree that made each change as the commit's author. `git blame` names the decree behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `mx/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución Política de los Estados Unidos Mexicanos (1917) | 117 | From the text in force on 8 April 2006 (the oldest copy available, after the reform published in the DOF on 7 April 2006) to the reform of 7 October 2026: reforms 167 to 285, every one with its own commit |
| `lfpdppp/` | Ley Federal de Protección de Datos Personales en Posesión de los Particulares | 3 | The law of 2010 as enacted (in force 6 July 2010, never amended), the new law of the same name that replaced it (DOF 20 March 2025, in force 21 March 2025), and its reform of 14 November 2025 |
| `codigo-civil-federal/` | Código Civil Federal (1928) | 14 | From the text in force on 1 January 2005 (the oldest copy available) to the reform of 14 November 2025 |
| `codigo-penal-federal/` | Código Penal Federal (1931) | 70 | From 1 July 2006 to the reform of 13 March 2026 |
| `codigo-de-comercio/` | Código de Comercio (1889) | 37 | From 7 June 2006 to the Acuerdo of 18 February 2026 updating its amounts |
| `codigo-federal-de-procedimientos-civiles/` | Código Federal de Procedimientos Civiles (1943) | 11 | From 14 June 2003 to the SCJN ruling published on 5 June 2025 |
| `codigo-fiscal-de-la-federacion/` | Código Fiscal de la Federación (1981) | 33 | From 19 July 2006 to the reform of 9 April 2026 |
| `codigo-nacional-de-procedimientos-penales/` | Código Nacional de Procedimientos Penales (2014) | 16 | The code as enacted (DOF 5 March 2014) to the reform of 28 November 2025 |
| `codigo-nacional-de-procedimientos-civiles-y-familiares/` | Código Nacional de Procedimientos Civiles y Familiares (2023) | 5 | The code as enacted (in force 8 June 2023) to the reform of 15 January 2026 |
| `ley-federal-del-trabajo/` | Ley Federal del Trabajo (1970) | 30 | From 18 January 2006 to the reform of 14 May 2026 |
| `ley-de-amparo/` | Ley de Amparo (2013) | 12 | The law as enacted (in force 3 April 2013) to the reform of 16 October 2025 |
| `ley-general-de-sociedades-mercantiles/` | Ley General de Sociedades Mercantiles (1934) | 11 | From 29 July 2006 to the Acuerdo of 26 December 2025 |
| `ley-general-de-titulos-y-operaciones-de-credito/` | Ley General de Títulos y Operaciones de Crédito (1932) | 9 | From 19 July 2006 to the reform of 26 March 2024 |
| `ley-de-instituciones-de-credito/` | Ley de Instituciones de Crédito (1990) | 22 | From 19 July 2006 to the reform of 14 November 2025 |
| `ley-federal-de-proteccion-al-consumidor/` | Ley Federal de Protección al Consumidor (1992) | 40 | From 1 January 2007 to the Acuerdo updating its amounts for 2026 |
| `ley-de-concursos-mercantiles/` | Ley de Concursos Mercantiles (2000) | 8 | The law as enacted (in force 13 May 2000) to the SCJN ruling published on 16 January 2026 |
| `ley-del-mercado-de-valores/` | Ley del Mercado de Valores (2005) | 8 | From 29 June 2007 to the reform of 14 November 2025 |
| `ley-del-seguro-social/` | Ley del Seguro Social (1995) | 34 | From 12 August 2006 to the reform of 15 January 2026 |
| `ley-general-de-salud/` | Ley General de Salud (1984) | 94 | From 7 June 2006 to the reform of 15 January 2026 |
| `ley-del-issste/` | Ley del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (2007) | 22 | The law as enacted (in force 1 April 2007) to the reform of 15 January 2026 |
| `ley-federal-de-procedimiento-administrativo/` | Ley Federal de Procedimiento Administrativo (1994) | 6 | From 31 May 2000 to the reform of 14 November 2025 |
| `ley-agraria/` | Ley Agraria (1992) | 14 | From 10 July 1993 to the reform of 14 November 2025 |
| `ley-de-migracion/` | Ley de Migración (2011) | 19 | The law as enacted (in force 26 May 2011) to the reform of 15 January 2026 |
| `ley-general-de-educacion/` | Ley General de Educación (2019) | 7 | The law as enacted (in force 1 October 2019) to the reform of 15 January 2026 |
| `ley-del-impuesto-sobre-la-renta/` | Ley del Impuesto sobre la Renta (2013) | 9 | The law as enacted (in force 1 January 2014) to the reform of 1 April 2024 |
| `ley-del-impuesto-al-valor-agregado/` | Ley del Impuesto al Valor Agregado (1978) | 10 | From 19 July 2006 to the reform of 12 November 2021 |
| `ley-aduanera/` | Ley Aduanera (1995) | 12 | From 3 February 2006 to the reform of 19 November 2025 |
| `ley-federal-del-derecho-de-autor/` | Ley Federal del Derecho de Autor (1996) | 15 | From 24 July 2003 to the reform of 14 May 2026 |
| `ley-federal-de-proteccion-a-la-propiedad-industrial/` | Ley Federal de Protección a la Propiedad Industrial (2020) | 4 | The law as enacted (in force 5 November 2020) to the reform of 3 April 2026 |
| `ley-general-de-responsabilidades-administrativas/` | Ley General de Responsabilidades Administrativas (2016) | 10 | The law as enacted (in force 19 July 2017) to the reform of 15 December 2025 |
| `ley-nacional-de-ejecucion-penal/` | Ley Nacional de Ejecución Penal (2016) | 3 | The law as enacted (in force 17 June 2016) to the reform of 1 April 2024 |
| `ley-federal-de-competencia-economica/` | Ley Federal de Competencia Económica (2014) | 5 | The law as enacted (in force 7 July 2014) to the reform of 14 November 2025 |
| `ley-general-de-transparencia/` | Ley General de Transparencia y Acceso a la Información Pública (2025) | 1 | The law as enacted (in force 21 March 2025); the newest copy available (July 2025) prints no reform |
| `ley-general-de-instituciones-y-procedimientos-electorales/` | Ley General de Instituciones y Procedimientos Electorales (2014) | 10 | The law as enacted (in force 24 May 2014) to the reform of 2 June 2026 |
| `ley-general-del-equilibrio-ecologico/` | Ley General del Equilibrio Ecológico y la Protección al Ambiente (1988) | 38 | From 24 May 2006 to the reform of 19 January 2026 |
| `ley-de-instituciones-de-seguros-y-de-fianzas/` | Ley de Instituciones de Seguros y de Fianzas (2013) | 5 | The law as enacted (in force 4 April 2015) to the reform of 14 November 2025 |
| `ley-general-de-acceso-de-las-mujeres/` | Ley General de Acceso de las Mujeres a una Vida Libre de Violencia (2007) | 27 | The law as enacted (in force 2 February 2007) to the reform of 15 January 2026 |
| `ley-general-de-los-derechos-de-ninas-ninos-y-adolescentes/` | Ley General de los Derechos de Niñas, Niños y Adolescentes (2014) | 23 | The law as enacted (in force 5 December 2014) to the reform of 15 January 2026 |
| `ley-organica-de-la-administracion-publica-federal/` | Ley Orgánica de la Administración Pública Federal (1976) | 50 | From 3 June 2006 to the reform of 7 May 2026 |
| `ley-federal-de-presupuesto-y-responsabilidad-hacendaria/` | Ley Federal de Presupuesto y Responsabilidad Hacendaria (2006) | 21 | From 1 January 2007 to the reform of 9 April 2026 |
| `ley-de-aguas-nacionales/` | Ley de Aguas Nacionales (1992) | 11 | From 30 April 2004 to the reform of 11 December 2025 |
| `ley-de-coordinacion-fiscal/` | Ley de Coordinación Fiscal (1978) | 14 | From 1 January 2007 to the reform of 3 January 2024 |
| `ley-del-impuesto-especial-sobre-produccion-y-servicios/` | Ley del Impuesto Especial sobre Producción y Servicios (1980) | 24 | From 1 January 2007 to the Acuerdo of 22 December 2025 |
| `ley-del-infonavit/` | Ley del Instituto del Fondo Nacional de la Vivienda para los Trabajadores (1972) | 17 | From 4 June 2005 to the reform of 21 February 2025 |
| `ley-general-de-bienes-nacionales/` | Ley General de Bienes Nacionales (2004) | 14 | The law as enacted (in force 21 May 2004) to the reform of 14 November 2025 |
| `ley-general-de-cambio-climatico/` | Ley General de Cambio Climático (2012) | 13 | The law as enacted (in force 10 October 2012) to the reform of 1 April 2024 |
| `ley-federal-contra-la-delincuencia-organizada/` | Ley Federal contra la Delincuencia Organizada (1996) | 18 | From 28 March 2007 to the reform of 28 November 2025 |
| `ley-organica-del-congreso-general/` | Ley Orgánica del Congreso General de los Estados Unidos Mexicanos (1999) | 31 | From 14 September 2006 to the reform of 7 July 2025 |
| `ley-organica-del-poder-judicial-de-la-federacion/` | Ley Orgánica del Poder Judicial de la Federación (2024) | 2 | The law as enacted (in force 21 December 2024) to the reform of 28 November 2025 |
| `ley-de-adquisiciones-arrendamientos-y-servicios/` | Ley de Adquisiciones, Arrendamientos y Servicios del Sector Público (2025) | 1 | The law as enacted (in force 17 April 2025); the newest copy available (May 2025) prints no reform |
| `ley-de-inversion-extranjera/` | Ley de Inversión Extranjera (1993) | 12 | From 19 July 2006 to the reform of 27 May 2024 |
| `ley-general-de-poblacion/` | Ley General de Población (1974) | 12 | From 5 January 1999 to the reform of 16 July 2025 |
| `ley-federal-de-armas-de-fuego-y-explosivos/` | Ley Federal de Armas de Fuego y Explosivos (1972) | 7 | From 24 January 2004 to the reform of 29 May 2025 |
| `ley-general-del-sistema-nacional-de-seguridad-publica/` | Ley General del Sistema Nacional de Seguridad Pública (2025) | 1 | The law as enacted (in force 17 July 2025); the newest copy available (January 2026) prints no reform |
| `ley-federal-de-las-entidades-paraestatales/` | Ley Federal de las Entidades Paraestatales (1986) | 12 | From 22 August 2006 to the reform of 16 July 2025 |
| `ley-general-de-vida-silvestre/` | Ley General de Vida Silvestre (2000) | 22 | From 4 February 2007 to the reform of 16 July 2025 |
| `ley-general-de-proteccion-civil/` | Ley General de Protección Civil (2012) | 9 | The law as enacted (in force 7 June 2012) to the reform of 21 December 2023 |
| `ley-de-vivienda/` | Ley de Vivienda (2006) | 11 | The law as enacted (in force 28 June 2006) to the reform of 29 April 2026 |
| `ley-general-de-partidos-politicos/` | Ley General de Partidos Políticos (2014) | 7 | The law as enacted (in force 24 May 2014) to the SCJN ruling published on 24 November 2023 |
| `ley-general-del-sistema-de-medios-de-impugnacion/` | Ley General del Sistema de Medios de Impugnación en Materia Electoral (1996) | 12 | The law as enacted (in force 22 November 1996) to the reform of 14 November 2025 |
| `ley-general-de-contabilidad-gubernamental/` | Ley General de Contabilidad Gubernamental (2008) | 11 | The law as enacted (in force 1 January 2009) to the reform of 14 May 2026 |
| `ley-general-de-mecanismos-alternativos/` | Ley General de Mecanismos Alternativos de Solución de Controversias (2024) | 1 | The law as enacted (in force 27 January 2024); the newest copy available (October 2024) prints no reform |
| `ley-federal-de-responsabilidad-patrimonial-del-estado/` | Ley Federal de Responsabilidad Patrimonial del Estado (2004) | 5 | The law as enacted (in force 1 January 2005) to the reform of 29 December 2023 |
| `ley-de-asociaciones-religiosas-y-culto-publico/` | Ley de Asociaciones Religiosas y Culto Público (1992) | 4 | From 25 April 2006 to the reform of 17 December 2015 |
| `ley-general-de-pesca-y-acuacultura-sustentables/` | Ley General de Pesca y Acuacultura Sustentables (2007) | 16 | The law as enacted (in force 22 October 2007) to the reform of 1 April 2024 |
| `ley-de-fondos-de-inversion/` | Ley de Fondos de Inversión (2001) | 8 | From 29 January 2004 to the reform of 14 November 2025 |
| `ley-general-de-desarrollo-social/` | Ley General de Desarrollo Social (2004) | 12 | The law as enacted (in force 21 January 2004) to the reform of 15 January 2026 |
| `ley-general-de-archivos/` | Ley General de Archivos (2018) | 4 | The law as enacted (in force 15 June 2019) to the reform of 14 November 2025 |
| `ley-general-de-victimas/` | Ley General de Víctimas (2013) | 9 | The law as enacted (in force 8 February 2013) to the reform of 1 April 2024 |
| `ley-general-de-asentamientos-humanos/` | Ley General de Asentamientos Humanos, Ordenamiento Territorial y Desarrollo Urbano (2016) | 6 | The law as enacted (in force 29 November 2016) to the reform of 1 April 2024 |
| `ley-del-sector-hidrocarburos/` | Ley del Sector Hidrocarburos (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (May 2025) prints no reform |
| `ley-del-sector-electrico/` | Ley del Sector Eléctrico (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (June 2025) prints no reform |
| `ley-general-de-educacion-superior/` | Ley General de Educación Superior (2021) | 1 | The law as enacted (in force 21 April 2021); the newest copy available (October 2021) prints no reform |
| `ley-general-de-movilidad-y-seguridad-vial/` | Ley General de Movilidad y Seguridad Vial (2022) | 3 | The law as enacted (in force 18 May 2022) to the reform of 29 December 2023 |
| `ley-general-de-turismo/` | Ley General de Turismo (2009) | 14 | The law as enacted (in force 18 June 2009) to the publication of 14 November 2025 |
| `ley-general-para-la-igualdad-entre-mujeres-y-hombres/` | Ley General para la Igualdad Sustantiva entre Mujeres y Hombres (2006) | 19 | The law as enacted (in force 3 August 2006) to the reform of 15 January 2026 |
| `ley-general-para-la-inclusion-de-las-personas-con-discapacidad/` | Ley General para la Inclusión de las Personas con Discapacidad (2011) | 10 | The law as enacted (in force 31 May 2011) to the reform of 14 June 2024 |
| `ley-nacional-del-sistema-integral-de-justicia-penal-para-adolescentes/` | Ley Nacional del Sistema Integral de Justicia Penal para Adolescentes (2016) | 3 | The law as enacted (in force 18 June 2016) to the reform of 20 December 2022 |
| `ley-general-de-proteccion-de-datos-personales-sujetos-obligados/` | Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (2025) | 2 | The law as enacted (in force 21 March 2025) to the reform of 14 November 2025 |
| `ley-de-los-sistemas-de-ahorro-para-el-retiro/` | Ley de los Sistemas de Ahorro para el Retiro (1996) | 10 | From 12 January 2005 to the reform of 14 November 2025 |
| `ley-nacional-de-extincion-de-dominio/` | Ley Nacional de Extinción de Dominio (2019) | 5 | The law as enacted (in force 10 August 2019) to the reform of 28 November 2025 |
| `ley-nacional-sobre-el-uso-de-la-fuerza/` | Ley Nacional sobre el Uso de la Fuerza (2019) | 3 | The law as enacted (in force 28 May 2019) to the reform of 24 January 2024 |
| `ley-de-la-guardia-nacional/` | Ley de la Guardia Nacional (2025) | 1 | The law as enacted (in force 17 July 2025); the newest copy available (February 2026) prints no reform |
| `ley-de-planeacion/` | Ley de Planeación (1983) | 9 | From 14 June 2003 to the reform of 15 January 2026 |
| `ley-de-los-derechos-de-las-personas-adultas-mayores/` | Ley de los Derechos de las Personas Adultas Mayores (2002) | 15 | From 12 March 2006 to the reform of 14 June 2024 |
| `ley-federal-de-seguridad-privada/` | Ley Federal de Seguridad Privada (2006) | 4 | The law as enacted (in force 7 July 2006) to the reform of 17 October 2011 |
| `ley-minera/` | Ley Minera (1992) | 4 | From 27 June 2006 to the reform of 8 May 2023 |
| `ley-de-ingresos-sobre-hidrocarburos/` | Ley de Ingresos sobre Hidrocarburos (2014) | 6 | The law as enacted (in force 12 August 2014) to the reform of 18 March 2025 |
| `ley-federal-de-procedimiento-contencioso-administrativo/` | Ley Federal de Procedimiento Contencioso Administrativo (2005) | 13 | The law as enacted (in force 1 January 2006) to the reform of 9 June 2026 |
| `ley-general-del-sistema-nacional-anticorrupcion/` | Ley General del Sistema Nacional Anticorrupción (2016) | 2 | The law as enacted (in force 19 July 2016) to the reform of 20 May 2021 |
| `ley-de-fiscalizacion-y-rendicion-de-cuentas/` | Ley de Fiscalización y Rendición de Cuentas de la Federación (2016) | 5 | The law as enacted (in force 19 July 2016) to the erratum of 15 May 2026 |
| `ley-organica-del-tribunal-federal-de-justicia-administrativa/` | Ley Orgánica del Tribunal Federal de Justicia Administrativa (2016) | 3 | The law as enacted (in force 19 July 2016) to the reform of 16 October 2025 |
| `ley-de-la-fiscalia-general-de-la-republica/` | Ley de la Fiscalía General de la República (2021) | 4 | The law as enacted (in force 21 May 2021) to the reform of 14 November 2025 |
| `ley-de-comercio-exterior/` | Ley de Comercio Exterior (1993) | 3 | From 25 January 2006 to the reform of 1 May 2026 |
| `ley-federal-de-los-derechos-del-contribuyente/` | Ley Federal de los Derechos del Contribuyente (2005) | 1 | The law as enacted (in force 23 July 2005); the newest copy available (February 2019) prints no reform |
| `ley-de-seguridad-nacional/` | Ley de Seguridad Nacional (2005) | 7 | From 27 December 2005 to the reform of 14 November 2025 |
| `ley-federal-de-remuneraciones-de-los-servidores-publicos/` | Ley Federal de Remuneraciones de los Servidores Públicos (2021) | 1 | The law as enacted (in force 20 May 2021); the newest copy available (February 2023) prints no reform |
| `ley-general-de-sociedades-cooperativas/` | Ley General de Sociedades Cooperativas (1994) | 5 | From 5 June 2001 to the reform of 16 April 2025 |
| `ley-de-nacionalidad/` | Ley de Nacionalidad (1998) | 2 | From 13 January 2005 to the reform of 23 April 2012 |
| `ley-del-banco-de-mexico/` | Ley del Banco de México (1993) | 4 | From 1 January 2001 to the reform of 10 January 2014 |
| `ley-de-la-comision-nacional-de-los-derechos-humanos/` | Ley de la Comisión Nacional de los Derechos Humanos (1992) | 15 | From 1 July 2006 to the reform of 1 April 2024 |
| `ley-federal-para-prevenir-y-eliminar-la-discriminacion/` | Ley Federal para Prevenir y Eliminar la Discriminación (2003) | 19 | The law as enacted (in force 12 June 2003) to the reform of 14 November 2025 |
| `ley-de-desarrollo-rural-sustentable/` | Ley de Desarrollo Rural Sustentable (2001) | 15 | The law as enacted (in force 8 December 2001) to the reform of 7 June 2024 |
| `ley-general-de-desarrollo-forestal-sustentable/` | Ley General de Desarrollo Forestal Sustentable (2018) | 7 | The law as enacted (in force 6 June 2018) to the reform of 1 April 2024 |
| `ley-federal-de-sanidad-animal/` | Ley Federal de Sanidad Animal (2007) | 5 | The law as enacted (in force 26 July 2007) to the reform of 21 May 2024 |
| `ley-de-caminos-puentes-y-autotransporte-federal/` | Ley de Caminos, Puentes y Autotransporte Federal (1993) | 16 | From 26 October 2005 to the reform of 14 November 2025 |
| `ley-de-aeropuertos/` | Ley de Aeropuertos (1995) | 9 | From 6 July 2006 to the reform of 14 November 2025 |
| `ley-de-puertos/` | Ley de Puertos (1993) | 7 | The law as enacted (in force 20 July 1993) to the reform of 7 December 2020 |
| `ley-de-navegacion-y-comercio-maritimos/` | Ley de Navegación y Comercio Marítimos (2006) | 8 | The law as enacted (in force 4 June 2006) to the reform of 14 November 2025 |
| `ley-organica-del-ejercito-y-fuerza-aerea-mexicanos/` | Ley Orgánica del Ejército y Fuerza Aérea Mexicanos (1986) | 15 | From 20 March 1998 to the reform of 16 July 2025 |
| `ley-organica-de-la-armada-de-mexico/` | Ley Orgánica de la Armada de México (2025) | 1 | The law as enacted (in force 8 November 2025); the newest copy available (November 2025) prints no reform |
| `ley-de-obras-publicas-y-servicios-relacionados/` | Ley de Obras Públicas y Servicios Relacionados con las Mismas (2000) | 11 | From 8 July 2005 to the reform of 14 November 2025 |
| `ley-de-asociaciones-publico-privadas/` | Ley de Asociaciones Público Privadas (2012) | 7 | The law as enacted (in force 17 January 2012) to the reform of 14 November 2025 |
| `ley-de-vias-generales-de-comunicacion/` | Ley de Vías Generales de Comunicación (1940) | 10 | From 26 October 2005 to the reform of 14 November 2025 |
| `ley-del-servicio-exterior-mexicano/` | Ley del Servicio Exterior Mexicano (1994) | 4 | From 26 January 2002 to the reform of 19 April 2018 |
| `ley-federal-de-juegos-y-sorteos/` | Ley Federal de Juegos y Sorteos (1947) | 1 | The law as enacted (in force 5 January 1948); the newest copy available (February 2019) prints no reform |
| `ley-de-bioseguridad-de-organismos-geneticamente-modificados/` | Ley de Bioseguridad de Organismos Genéticamente Modificados (2005) | 3 | The law as enacted (in force 2 May 2005) to the reform of 11 May 2022 |
| `ley-federal-de-variedades-vegetales/` | Ley Federal de Variedades Vegetales (1996) | 3 | The law as enacted (in force 26 October 1996) to the reform of 11 May 2022 |
| `ley-general-de-cultura-y-derechos-culturales/` | Ley General de Cultura y Derechos Culturales (2017) | 7 | The law as enacted (in force 20 June 2017) to the publication of 15 January 2026 |
| `ley-general-de-cultura-fisica-y-deporte/` | Ley General de Cultura Física y Deporte (2013) | 15 | The law as enacted (in force 8 June 2013) to the publication of 14 November 2025 |
| `ley-del-instituto-nacional-de-las-mujeres/` | Ley del Instituto Nacional de las Mujeres (2001) | 6 | The law as enacted (in force 13 January 2001) to the reform of 20 May 2021; abrogated in full on 16 January 2026 by the decree of 15 January 2026 reforming the Ley General para la Igualdad entre Mujeres y Hombres (the last commit removes every provision) |
| `ley-federal-de-fomento-a-las-actividades-de-osc/` | Ley Federal de Fomento a las Actividades Realizadas por Organizaciones de la Sociedad Civil (2004) | 8 | The law as enacted (in force 10 February 2004) to the reform of 1 April 2024 |
| `ley-federal-del-mar/` | Ley Federal del Mar (1986) | 1 | From 12 January 1986; the newest copy available (November 2018) prints no reform |
| `ley-de-energia-para-el-campo/` | Ley de Energía para el Campo (2002) | 2 | The law as enacted (in force 31 December 2002) to the reform of 28 December 2012 |
| `ley-reglamentaria-del-articulo-105/` | Ley Reglamentaria de las Fracciones I y II del Artículo 105 de la Constitución Política de los Estados Unidos Mexicanos (1995) | 8 | From 22 November 1996 to the reform of 14 November 2025 |
| `ley-general-contra-la-tortura/` | Ley General para Prevenir, Investigar y Sancionar la Tortura y Otros Tratos o Penas Crueles, Inhumanos o Degradantes (2017) | 3 | The law as enacted (in force 27 June 2017) to the reform of 28 April 2022 |
| `ley-general-en-materia-de-desaparicion/` | Ley General en Materia de Desaparición Forzada de Personas, Desaparición Cometida por Particulares y del Sistema Nacional de Búsqueda de Personas (2017) | 7 | The law as enacted (in force 16 January 2018) to the reform of 16 July 2025 |
| `ley-general-en-materia-de-trata-de-personas/` | Ley General para Prevenir, Sancionar y Erradicar los Delitos en Materia de Trata de Personas y para la Protección y Asistencia a las Víctimas de estos Delitos (2012) | 7 | The law as enacted (in force 15 June 2012) to the reform of 14 November 2025 |
| `ley-federal-de-defensoria-publica/` | Ley Federal de Defensoría Pública (1998) | 10 | The law as enacted (in force 29 May 1998) to the reform of 1 April 2024 |
| `ley-del-servicio-de-administracion-tributaria/` | Ley del Servicio de Administración Tributaria (1995) | 5 | From 13 June 2003 to the reform of 4 December 2018 |
| `ley-federal-de-deuda-publica/` | Ley Federal de Deuda Pública (1976) | 5 | From 1 January 1996 to the reform of 30 January 2018 |
| `ley-de-disciplina-financiera/` | Ley de Disciplina Financiera de las Entidades Federativas y los Municipios (2016) | 3 | The law as enacted (in force 28 April 2016) to the reform of 10 May 2022 |
| `ley-para-la-transparencia-de-los-servicios-financieros/` | Ley para la Transparencia y Ordenamiento de los Servicios Financieros (2007) | 7 | The law as enacted (in force 16 June 2007) to the publication of 14 November 2025 |
| `ley-de-proteccion-al-usuario-de-servicios-financieros/` | Ley de Protección y Defensa al Usuario de Servicios Financieros (1999) | 10 | From 7 June 2006 to the reform of 14 November 2025 |
| `ley-de-tecnologia-financiera/` | Ley para Regular las Instituciones de Tecnología Financiera (2018) | 4 | The law as enacted (in force 10 March 2018) to the reform of 14 November 2025 |
| `ley-general-de-organizaciones-auxiliares-del-credito/` | Ley General de Organizaciones y Actividades Auxiliares del Crédito (1985) | 10 | From 19 July 2006 to the reform of 14 November 2025 |
| `ley-del-sistema-nacional-de-informacion-estadistica/` | Ley del Sistema Nacional de Información Estadística y Geográfica (2008) | 10 | The law as enacted (in force 15 July 2008) to the reform of 14 November 2025 |
| `ley-federal-de-sanidad-vegetal/` | Ley Federal de Sanidad Vegetal (1994) | 6 | The law as enacted (in force 6 January 1994) to the reform of 11 May 2022 |
| `ley-reglamentaria-del-articulo-5-profesiones/` | Ley Reglamentaria del Artículo 5o. Constitucional, relativo al ejercicio de las profesiones en la Ciudad de México (1945) | 3 | From 1 January 1994 to the reform of 19 January 2018 |
| `ley-de-ahorro-y-credito-popular/` | Ley de Ahorro y Crédito Popular (2001) | 9 | From 19 July 2006 to the reform of 14 November 2025 |
| `ley-federal-de-consulta-popular/` | Ley Federal de Consulta Popular (2014) | 2 | The law as enacted (in force 15 March 2014) to the reform of 19 May 2021 |
| `ley-federal-de-revocacion-de-mandato/` | Ley Federal de Revocación de Mandato (2021) | 2 | The law as enacted (in force 15 September 2021) to the SCJN ruling published on 26 September 2022 |
| `ley-federal-de-austeridad-republicana/` | Ley Federal de Austeridad Republicana (2019) | 3 | The law as enacted (in force 20 November 2019) to the reform of 16 April 2025 |
| `ley-federal-de-responsabilidad-ambiental/` | Ley Federal de Responsabilidad Ambiental (2013) | 3 | The law as enacted (in force 7 July 2013) to the reform of 14 November 2025 |
| `ley-de-la-comision-nacional-bancaria-y-de-valores/` | Ley de la Comisión Nacional Bancaria y de Valores (1995) | 8 | From 21 June 2005 to the reform of 11 May 2022 |
| `ley-de-proteccion-al-ahorro-bancario/` | Ley de Protección al Ahorro Bancario (1999) | 4 | From 7 July 2006 to the reform of 11 May 2022 |
| `ley-de-uniones-de-credito/` | Ley de Uniones de Crédito (2008) | 4 | The law as enacted (in force 21 August 2008) to the publication of 14 November 2025 |
| `ley-del-issfam/` | Ley del Instituto de Seguridad Social para las Fuerzas Armadas Mexicanas (2003) | 12 | From 9 May 2006 to the SCJN ruling published on 16 December 2025 |
| `ley-de-productos-organicos/` | Ley de Productos Orgánicos (2006) | 1 | The law as enacted (in force 8 February 2006); the newest copy available (February 2019) prints no reform |
| `ley-de-sistemas-de-pagos/` | Ley de Sistemas de Pagos (2002) | 2 | The law as enacted (in force 13 December 2002) to the reform of 14 November 2025 |
| `ley-de-premios-estimulos-y-recompensas-civiles/` | Ley de Premios, Estímulos y Recompensas Civiles (1975) | 3 | From 30 March 2022 to the reform of 1 April 2024 |
| `ley-sobre-la-celebracion-de-tratados/` | Ley sobre la Celebración de Tratados (1992) | 2 | The law as enacted (in force 3 January 1992) to the reform of 20 May 2021 |
| `ley-de-asistencia-social/` | Ley de Asistencia Social (2004) | 10 | The law as enacted (in force 3 September 2004) to the reform of 1 April 2024 |
| `ley-de-expropiacion/` | Ley de Expropiación (1936) | 4 | From 5 December 1997 to the reform of 27 January 2012 |
| `ley-de-fomento-para-la-lectura-y-el-libro/` | Ley de Fomento para la Lectura y el Libro (2008) | 5 | The law as enacted (in force 25 July 2008) to the reform of 29 November 2023 |
| `ley-general-de-bibliotecas/` | Ley General de Bibliotecas (2021) | 2 | The law as enacted (in force 2 June 2021) to the reform of 29 November 2023 |
| `ley-federal-de-cinematografia/` | Ley Federal de Cinematografía (1992) | 7 | From 27 January 2006 to the SCJN ruling published on 19 August 2025; abrogated in full on 23 May 2026 by the Ley Federal de Cine y el Audiovisual (the last commit removes every provision) |
| `ley-de-educacion-militar/` | Ley de Educación Militar del Ejército, Fuerza Aérea y Guardia Nacional (2005) | 5 | The law as enacted (in force 24 December 2005) to the reform of 16 July 2025 |
| `ley-de-disciplina-del-ejercito/` | Ley de Disciplina del Ejército, Fuerza Aérea y Guardia Nacional (1926) | 3 | From 11 December 2004 to the reform of 16 July 2025 |
| `ley-de-ascensos-y-recompensas-del-ejercito/` | Ley de Ascensos y Recompensas del Ejército, Fuerza Aérea y Guardia Nacional (2003) | 11 | The law as enacted (in force 31 October 2003) to the reform of 16 July 2025 |
| `ley-de-ascensos-de-la-armada-de-mexico/` | Ley de Ascensos de la Armada de México (2004) | 7 | The law as enacted (in force 26 June 2004) to the reform of 17 December 2025 |
| `ley-de-firma-electronica-avanzada/` | Ley de Firma Electrónica Avanzada (2012) | 3 | The law as enacted (in force 2 July 2012) to the reform of 14 November 2025 |
| `ley-en-materia-de-telecomunicaciones-y-radiodifusion/` | Ley en materia de Telecomunicaciones y Radiodifusión (2025) | 1 | The law as enacted (in force 17 July 2025); the newest copy available (August 2025) prints no reform |
| `codigo-de-justicia-militar/` | Código de Justicia Militar (1933) | 8 | From 30 June 2005 to the reform of 16 July 2025 |
| `codigo-militar-de-procedimientos-penales/` | Código Militar de Procedimientos Penales (2016) | 6 | The law as enacted (in force 17 May 2016) to the reform of 14 November 2025 |
| `ley-general-de-residuos/` | Ley General para la Prevención y Gestión Integral de los Residuos (2003) | 15 | From 23 May 2006 to the reform of 19 January 2026 |
| `ley-general-de-humanidades-ciencias-tecnologias-e-innovacion/` | Ley General en materia de Humanidades, Ciencias, Tecnologías e Innovación (2023) | 1 | The law as enacted (in force 9 May 2023); the newest copy available (April 2024) prints no reform |
| `ley-del-instituto-nacional-de-los-pueblos-indigenas/` | Ley del Instituto Nacional de los Pueblos Indígenas (2018) | 4 | The law as enacted (in force 5 December 2018) to the reform of 29 December 2023 |
| `ley-de-tesoreria-de-la-federacion/` | Ley de Tesorería de la Federación (2015) | 1 | The law as enacted (in force 1 January 2016); the newest copy available (December 2018) prints no reform |
| `ley-sobre-el-contrato-de-seguro/` | Ley sobre el Contrato de Seguro (1935) | 4 | From 25 April 2006 to the reform of 4 April 2013 |
| `ley-general-de-comunicacion-social/` | Ley General de Comunicación Social (2018) | 6 | The law as enacted (in force 1 January 2019) to the reform of 1 April 2024 |
| `ley-monetaria/` | Ley Monetaria de los Estados Unidos Mexicanos (1931) | 3 | From 1 January 2006 to the reform of 19 January 2026 |
| `ley-de-sociedades-de-solidaridad-social/` | Ley de Sociedades de Solidaridad Social (1976) | 2 | The law as enacted (in force 28 May 1976) to the reform of 24 April 2018 |
| `ley-de-fomento-a-la-confianza-ciudadana/` | Ley de Fomento a la Confianza Ciudadana (2020) | 1 | The law as enacted (in force 21 January 2020); the newest copy available (August 2022) prints no reform |
| `ley-federal-del-impuesto-sobre-automoviles-nuevos/` | Ley Federal del Impuesto sobre Automóviles Nuevos (1996) | 11 | From 27 December 2005 to the publication of 10 January 2025 |
| `ley-federal-contra-el-lavado-de-dinero/` | Ley Federal para la Prevención e Identificación de Operaciones con Recursos de Procedencia Ilícita (2012) | 4 | The law as enacted (in force 17 July 2013) to the reform of 16 July 2025 |
| `ley-general-de-mejora-regulatoria/` | Ley General de Mejora Regulatoria (2018) | 3 | The law as enacted (in force 19 May 2018) to the reform of 20 May 2021; abrogated in full on 17 July 2025 by the Ley Nacional para Eliminar Trámites Burocráticos (the last commit removes every provision) |
| `ley-de-sociedades-de-informacion-crediticia/` | Ley para Regular las Sociedades de Información Crediticia (2002) | 7 | From 24 January 2004 to the reform of 24 January 2024 |
| `ley-de-cooperativas-de-ahorro-y-prestamo/` | Ley para Regular las Actividades de las Sociedades Cooperativas de Ahorro y Préstamo (2009) | 7 | From 24 August 2009 to the publication of 14 November 2025 |
| `ley-federal-de-precursores-quimicos/` | Ley Federal para el Control de Precursores Químicos, Productos Químicos Esenciales y Máquinas para Elaborar Cápsulas, Tabletas y/o Comprimidos (1997) | 8 | The law as enacted (in force 26 March 1998) to the reform of 3 May 2023 |
| `ley-de-declaracion-especial-de-ausencia/` | Ley Federal de Declaración Especial de Ausencia para Personas Desaparecidas (2018) | 3 | The law as enacted (in force 23 June 2018) to the reform of 1 April 2024 |
| `ley-general-de-derechos-linguisticos/` | Ley General de Derechos Lingüísticos de los Pueblos Indígenas (2003) | 10 | The law as enacted (in force 14 March 2003) to the reform of 18 October 2023 |
| `ley-general-en-materia-de-delitos-electorales/` | Ley General en Materia de Delitos Electorales (2014) | 5 | From 28 June 2014 to the reform of 20 May 2021 |
| `ley-general-para-el-control-del-tabaco/` | Ley General para el Control del Tabaco (2008) | 5 | The law as enacted (in force 28 August 2008) to the reform of 17 February 2022 |
| `ley-del-servicio-militar/` | Ley del Servicio Militar (1940) | 5 | From 20 March 1998 to the reform of 18 May 2022 |
| `ley-de-proteccion-a-personas-en-el-procedimiento-penal/` | Ley Federal para la Protección a Personas que Intervienen en el Procedimiento Penal (2012) | 4 | The law as enacted (in force 5 December 2012) to the reform of 20 May 2021 |
| `ley-general-de-servicios-de-cuidado-infantil/` | Ley General de Prestación de Servicios para la Atención, Cuidado y Desarrollo Integral Infantil (2011) | 7 | The law as enacted (in force 25 October 2011) to the reform of 1 April 2024 |
| `ley-general-de-prevencion-social-de-la-violencia/` | Ley General para la Prevención Social de la Violencia y la Delincuencia (2012) | 2 | The law as enacted (in force 25 January 2012) to the reform of 4 May 2021 |
| `ley-general-del-espectro-autista/` | Ley General para la Atención y Protección a Personas con la Condición del Espectro Autista (2015) | 2 | The law as enacted (in force 1 May 2015) to the SCJN ruling published on 27 May 2016 |
| `ley-federal-de-semillas/` | Ley Federal de Producción, Certificación y Comercio de Semillas (2007) | 2 | The law as enacted (in force 14 August 2007) to the reform of 11 May 2018 |
| `ley-de-proteccion-de-personas-defensoras-y-periodistas/` | Ley para la Protección de Personas Defensoras de Derechos Humanos y Periodistas (2012) | 4 | The law as enacted (in force 26 June 2012) to the reform of 28 April 2022 |
| `ley-de-planeacion-y-transicion-energetica/` | Ley de Planeación y Transición Energética (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (May 2025) prints no reform |
| `ley-federal-de-sustancias-quimicas/` | Ley Federal para el Control de Sustancias Químicas Susceptibles de Desvío para la Fabricación de Armas Químicas (2009) | 3 | From 6 July 2009 to the reform of 14 June 2024 |
| `ley-general-de-economia-circular/` | Ley General de Economía Circular (2026) | 1 | The law as enacted (in force 20 January 2026); the newest copy available (March 2026) prints no reform |
| `ley-de-desarrollo-sustentable-de-la-cafeticultura/` | Ley de Desarrollo Sustentable de la Cafeticultura (2025) | 1 | The law as enacted (in force 17 June 2026); the newest copy available (January 2026) prints no reform |
| `ley-reglamentaria-del-servicio-ferroviario/` | Ley Reglamentaria del Servicio Ferroviario (1995) | 9 | The law as enacted (in force 13 May 1995) to the reform of 14 November 2025 |
| `ley-nacional-para-eliminar-tramites-burocraticos/` | Ley Nacional para Eliminar Trámites Burocráticos (2025) | 1 | The law as enacted (in force 17 July 2025); the newest copy available (August 2025) prints no reform |
| `ley-del-fondo-mexicano-del-petroleo/` | Ley del Fondo Mexicano del Petróleo para la Estabilización y el Desarrollo (2014) | 4 | The law as enacted (in force 12 August 2014) to the reform of 18 March 2025 |
| `ley-general-de-aguas/` | Ley General de Aguas (2025) | 1 | The law as enacted (in force 12 December 2025); the newest copy available (January 2026) prints no reform |
| `ley-general-en-materia-de-extorsion/` | Ley General para Prevenir, Investigar y Sancionar los Delitos en Materia de Extorsión, Reglamentaria de la fracción XXI del artículo 73 de la Constitución Política de los Estados Unidos Mexicanos (2025) | 1 | The law as enacted (in force 29 November 2025); the newest copy available (December 2025) prints no reform |
| `ley-de-aviacion-civil/` | Ley de Aviación Civil (1995) | 9 | From 6 July 2006 to the reform of 14 November 2025 |
| `ley-nacional-de-mecanismos-alternativos-en-materia-penal/` | Ley Nacional de Mecanismos Alternativos de Solución de Controversias en Materia Penal (2014) | 3 | The law as enacted (DOF 29 December 2014; in force gradually with the Código Nacional de Procedimientos Penales, dated three days after publication) to the reform of 1 April 2024 |
| `ley-de-la-empresa-publica-petroleos-mexicanos/` | Ley de la Empresa Pública del Estado, Petróleos Mexicanos (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (May 2025) prints no reform |
| `ley-de-la-empresa-publica-cfe/` | Ley de la Empresa Pública del Estado, Comisión Federal de Electricidad (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (June 2025) prints no reform |
| `ley-federal-sobre-monumentos-y-zonas-arqueologicos/` | Ley Federal sobre Monumentos y Zonas Arqueológicos, Artísticos e Históricos (1972) | 7 | From 14 January 1986 to the reform of 14 November 2025 |
| `ley-para-regular-las-agrupaciones-financieras/` | Ley para Regular las Agrupaciones Financieras (2014) | 4 | The law as enacted (in force 11 January 2014) to the reform of 14 November 2025 |
| `ley-federal-para-la-administracion-y-enajenacion-de-bienes/` | Ley Federal para la Administración y Enajenación de Bienes del Sector Público (2002) | 7 | From 24 February 2005 to the reform of 30 April 2024 |
| `ley-de-extradicion-internacional/` | Ley de Extradición Internacional (1975) | 3 | From 19 May 1999 to the reform of 20 May 2021 |
| `ley-de-la-economia-social-y-solidaria/` | Ley de la Economía Social y Solidaria (2012) | 8 | The law as enacted (in force 24 May 2012) to the reform of 16 April 2025 |
| `ley-de-geotermia/` | Ley de Geotermia (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (December 2025) prints no reform |
| `ley-de-biocombustibles/` | Ley de Biocombustibles (2025) | 1 | The law as enacted (in force 19 March 2025); the newest copy available (January 2026) prints no reform |
| `ley-del-sistema-nacional-de-investigacion-e-inteligencia/` | Ley del Sistema Nacional de Investigación e Inteligencia en Materia de Seguridad Pública (2025) | 1 | The law as enacted (in force 17 July 2025); the newest copy available (November 2025) prints no reform |
| `ley-de-infraestructura-de-la-calidad/` | Ley de Infraestructura de la Calidad (2020) | 1 | The law as enacted (in force 30 August 2020); the newest copy available (September 2020) prints no reform |
| `ley-del-sistema-publico-de-radiodifusion/` | Ley del Sistema Público de Radiodifusión del Estado Mexicano (2014) | 6 | The law as enacted (in force 13 August 2014) to the reform of 14 November 2025 |
| `ley-federal-de-cine-y-el-audiovisual/` | Ley Federal de Cine y el Audiovisual (2026) | 1 | The law as enacted (in force 23 May 2026); the newest copy available (June 2026) prints no reform |
| `ley-de-carrera-judicial/` | Ley de Carrera Judicial del Poder Judicial de la Federación (2025) | 1 | The law as enacted (in force 3 January 2025); the newest copy available (February 2026) prints no reform |
| `ley-del-instituto-mexicano-de-la-juventud/` | Ley del Instituto Mexicano de la Juventud (1999) | 7 | From 23 June 2006 to the reform of 1 April 2024 |
| `ley-de-los-institutos-nacionales-de-salud/` | Ley de los Institutos Nacionales de Salud (2000) | 8 | From 23 June 2006 to the reform of 11 May 2022 |
| `ley-de-cooperacion-internacional-para-el-desarrollo/` | Ley de Cooperación Internacional para el Desarrollo (2011) | 3 | The law as enacted (in force 16 April 2011) to the reform of 6 November 2020 |
| `ley-de-camaras-empresariales/` | Ley de Cámaras Empresariales y sus Confederaciones (2005) | 3 | The law as enacted (in force 21 January 2005) to the reform of 12 April 2019 |
| `ley-para-el-fomento-de-la-inversion-en-infraestructura/` | Ley para el Fomento de la Inversión en Infraestructura Estratégica para el Desarrollo con Bienestar (2026) | 1 | The law as enacted (in force 10 April 2026); the newest copy available (May 2026) prints no reform |
| `ley-de-responsabilidad-civil-por-danos-nucleares/` | Ley de Responsabilidad Civil por Daños Nucleares (1974) | 2 | The law as enacted (in force 1 January 1975) to the reform of 14 November 2025 |
| `ley-de-desarrollo-sustentable-de-la-cana-de-azucar/` | Ley de Desarrollo Sustentable de la Caña de Azúcar (2005) | 4 | The law as enacted (in force 23 August 2005) to the reform of 14 November 2025 |
| `ley-del-servicio-postal-mexicano/` | Ley del Servicio Postal Mexicano (1986) | 5 | The law as enacted (in force 24 March 1987) to the reform of 19 January 2023 |
| `ley-del-registro-publico-vehicular/` | Ley del Registro Público Vehicular (2004) | 4 | The law as enacted (in force 2 September 2004) to the reform of 20 May 2021 |
| `ley-de-transparencia-en-el-credito-garantizado/` | Ley de Transparencia y de Fomento a la Competencia en el Crédito Garantizado (2002) | 4 | From 8 February 2005 to the reform of 10 January 2014 |
| `ley-de-la-casa-de-moneda-de-mexico/` | Ley de la Casa de Moneda de México (1986) | 3 | From 27 January 1986 to the reform of 11 May 2022 |
| `ley-federal-para-el-fomento-de-la-microindustria/` | Ley Federal para el Fomento de la Microindustria y la Actividad Artesanal (1988) | 5 | From 23 July 1991 to the reform of 27 March 2023 |
| `ley-general-para-la-deteccion-oportuna-del-cancer/` | Ley General para la Detección Oportuna del Cáncer en la Infancia y la Adolescencia (2021) | 1 | The law as enacted (in force 8 January 2021); the newest copy available (February 2021) prints no reform |
| `ley-de-proteccion-del-espacio-aereo-mexicano/` | Ley de Protección del Espacio Aéreo Mexicano (2023) | 1 | The law as enacted (in force 2 March 2023); the newest copy available (March 2023) prints no reform |
| `ley-de-educacion-naval/` | Ley de Educación Naval (2019) | 2 | The law as enacted (in force 13 March 2019) to the reform of 24 March 2023 |
| `ley-de-fondos-de-aseguramiento-agropecuario/` | Ley de Fondos de Aseguramiento Agropecuario y Rural (2005) | 1 | The law as enacted (in force 14 May 2005); the newest copy available (February 2019) prints no reform |
| `ley-de-fomento-a-la-industria-vitivinicola/` | Ley de Fomento a la Industria Vitivinícola (2018) | 1 | The law as enacted (in force 24 May 2018); the newest copy available (January 2019) prints no reform |
| `ley-del-impuesto-sobre-servicios-de-interes-publico/` | Impuesto sobre Servicios Expresamente Declarados de Interés Público por Ley, en los que Intervengan Empresas Concesionarias de Bienes del Dominio Directo de la Nación (1968) | 1 | The law as enacted (in force 1 July 1969); the newest copy available (November 2018) prints no reform |
| `ley-reglamentaria-en-materia-nuclear/` | Ley Reglamentaria del Artículo 27 Constitucional en Materia Nuclear (1985) | 2 | From 20 March 1998 to the reform of 9 April 2012 |

The per-act `README.md` in each folder lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 82 of the Constitution say on 1 January 2020? | `python tools/en_vigor_el.py 2020-01-01 constitucion 82` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" main -- constitucion/art-082.md):constitucion/art-082.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" main -- constitucion/art-082.md; git show "$($r):constitucion/art-082.md"` |
| Which decree wrote each paragraph of art. 41? | `git blame constitucion/art-041.md` |
| Every change to art. 41, word by word | `git log -p --word-diff constitucion/art-041.md` |
| Every decree in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one decree changed | `git show law/decreto-cpeum-285` (tags `law/<key>` mark each decree's commit) |
| The whole Constitution on a date | `python tools/en_vigor_el.py 2010-01-01 constitucion` |
| The text on a version's day | `git show constitucion/2014-02-11` (tags `<act>/<in-force day>`) |
| A decree's own transitorios (in-force rules, deadlines) | `constitucion/transitorios-<DOF date>-<reform number>.md` |
| Decrees published but not yet in force | `git log main..futuro` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Mexico_City, on the day the change took effect** (the in-force date). The DOF publication date is the `Published:` trailer, and the in-force day is in `In-force:`, which the tools read.
- **The in-force day is read from each decree's own first transitorio**: for reforms 167 to 285, "entrará en vigor al día siguiente de su publicación" is the day after publication (116 decrees), "el día de su publicación" the same day (2), and "a los 120 días de su publicación" 120 days later (1, reform 193). A fixed date in the transitorio would be used as given.
- **Default rule.** Código Civil Federal art. 3: laws "obligan y surten sus efectos tres días después de su publicación en el periódico oficial"; art. 4: a law that fixes the day it starts binds from that day. The default is used only where no transitorio can be read (the erratum of 25 June 2009).
- **Terms read by hand.** Where a decree counts its start in business days ("día hábil siguiente", "noventa días hábiles"), in months or a year, from the next fiscal year, or in wording the general reader misses, its in-force day was read from its own transitorio, decree by decree; each such date is listed in the act's decisions in `REPRODUCE.md`.
- **Staggered dates are not split.** Some decrees put single provisions in force later (for example the political-electoral reform of 10 February 2014, whose provisions on arts. 65, 69, 74, 76, 83 and 89 start on 1 December 2018). Here the whole article changes on the decree's general in-force day; the later dates are in the decree's transitorios file, which is part of the record.
- **The Cámara prints a reform the day it is published**; here it appears only on its in-force day, so no wording appears before its decree applies.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- **Against the official text today:** for every act the last version equals the Cámara de Diputados' newest consolidated text available, which includes the last publication its reform list names; read a second, independent way (plain text, notes removed), each newest copy contains every unit paragraph verbatim. For the Constitution: the last version equals the consolidated text as archived on 10 October 2026 (last reform DOF 07-10-2026), provision by provision. Read a second, independent way (plain text, notes removed), that copy contains every one of the record's 4,100 paragraphs verbatim, and they cover 99.9% of its body text; the rest is the cover page and the Cámara's notes. The same check passes for all 78 copies used (223,778 paragraphs, none missing).
- Every version carries the sha256 of the archived PDF it was read from and the capture's address.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the decree that made the change, with an e-mail address that cannot exist (`decreto-cpeum-285@diputados.invalid`), so `git blame` and `git log --author` name decrees. Decrees are numbered as in the Cámara's chronological list of constitutional reforms. The committer is always Lexifina.

- **Credits come only from the source.** From 2013 the Cámara marks each paragraph with the reforms that touched it ("Párrafo reformado DOF 10-06-2011, 29-01-2016"). A changed provision is credited to a decree when such a note, in that copy or any later one, gives the DOF date of a decree published between the two copies compared. When several decrees were published that day, it is credited only if exactly one decree's title fits the article. Each decree's transitorios file is credited to that decree.
- **SCJN rulings, errata and Acuerdos.** Rulings of the Suprema Corte that strike provisions (declaratorias generales de inconstitucionalidad, acciones de inconstitucionalidad) are commits of their own, authored by the ruling and dated on its DOF publication; so are errata and the Acuerdos that update amounts set in a law (for example in the Código de Comercio and the Ley Federal de Protección al Consumidor). The Cámara's cover date ("Última reforma") does not move for them, so a copy is read as running to the latest such publication printed before it was archived.
- **One decree, several acts.** A decree that reforms several of these acts (for example the homologation decree of 14 November 2025) has one key and one author across them; each act gets its own commit for it.
- **Unexplained changes** are committed by the publisher, the Cámara de Diputados, and labelled "unexplained" (17 commits): mostly the Cámara's own proofreading (accents, commas, "sic" notes, in 2008 and 2013), transitorios of 1993-2004 decrees that it added to its compilation in 2020, and three changes that two decrees of the same day could each have made (art. 73 on 12 October 2011, art. 43 on 17 May 2021, art. 41 on 2 June 2026).
- **Errata** ("Fe de erratas") printed in the DOF are commits of their own; the erratum of 25 June 2009 corrects art. 16.
- Blame credits whole lines (one paragraph per line). In a provision written by several decrees, use `git log -p --word-diff` to see exactly which words each changed.

## What it does not show

- **The Constitution before April 2006.** The Cámara de Diputados keeps only the current text and each decree as published; the oldest consolidated copy the Internet Archive holds runs to the reform of 7 April 2006. The first commit is "oldest version available" and names the 170 earlier decrees (1917-2006); that history is not rebuilt.
- **The text between two archived copies.** For the Constitution 98 distinct copies exist (2006-2026); 8 were cut off by the archive at 1 MiB and are not used, and for each reform date the newest copy is used (78). The codes and laws follow the same rule (the copies used are listed in `REPRODUCE.md`). Where one copy is followed by several decrees, each decree's changes are separated only as far as the notes allow; a provision changed by two decrees between copies shows only its final wording, credited to both.
- **The Cámara's notes** are not in the text; they are used only to credit decrees.
- **Applicability data.** Where a transitorio says a provision applies only from a later election or to later cases, that is in the transitorios file, not in the dates.
- **Abrogated laws.** When an act in this record is abrogated in full by another act in it, its folder ends with a commit on the day the abrogation took effect that removes every provision, credited to the abrogating decree: the Ley Federal de Cinematografía, abrogated by the Ley Federal de Cine y el Audiovisual on 23 May 2026; the Ley General de Mejora Regulatoria, abrogated by the Ley Nacional para Eliminar Trámites Burocráticos on 17 July 2025; and the Ley del Instituto Nacional de las Mujeres, abrogated by the decree of 15 January 2026 that reformed the Ley General para la Igualdad entre Mujeres y Hombres, on 16 January 2026. Laws abrogated by acts outside this record are not closed.
- **The LFPDPPP as two laws.** The 2025 law abrogated the 2010 law and took its name; `lfpdppp/` shows both as one history, and the commit of 21 March 2025 replaces every article. Files with the same number (`art-016.md`) hold different laws' articles before and after that day.
- **The codes and laws before their oldest copy.** Each act starts at the oldest consolidated copy available (2003-2007 for most), or at the act as enacted where that copy is the enacted text (CNPP, CNPCF, Ley de Amparo, Ley de Concursos Mercantiles). The first commit names the earlier decrees the Cámara lists.
- **Laws that replaced a law of the same name.** The Ley General de Educación of 2019 and the Ley del Impuesto sobre la Renta of 2013 start as enacted; the laws they abrogated (Ley General de Educación of 1993, Ley del Impuesto sobre la Renta of 2002) are not in the record. The same holds for the Ley General de Transparencia y Acceso a la Información Pública of 2025 (the law of 2015 it abrogated is not included) and the Ley Federal de Protección a la Propiedad Industrial of 2020 (which replaced the Ley de la Propiedad Industrial of 1991). The Ley de Instituciones de Seguros y de Fianzas, published on 4 April 2013, starts on 4 April 2015, when it entered into force. The Ley Orgánica del Poder Judicial de la Federación of 2024, the Ley de Adquisiciones, Arrendamientos y Servicios del Sector Público of 2025 and the Ley General del Sistema Nacional de Seguridad Pública of 2025 also took the file name of the law of the same name they replaced; copies are told apart by their own cover, and the replaced laws (LOPJF 2021, LAASSP 2000, LGSNSP 2009) are not in the record. The same holds for the Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados of 2025 (the 2017 law is not included) and the Ley de la Guardia Nacional of 2025 (the 2019 law is not included), the Ley de Fiscalización y Rendición de Cuentas de la Federación of 2016 (the 2009 law is not included) and the Ley Federal de Remuneraciones de los Servidores Públicos of 2021 (the 2018 law is not included). The Ley General de Desarrollo Forestal Sustentable of 2018 is built from its own file name; the law of 2003 it replaced is not included. The Ley Orgánica de la Armada de México of 2025 replaced the law of the same name of 2021, which had replaced the law of 2002, all under one file name; neither earlier law is included. The Ley General de Cultura Física y Deporte of 2013 starts as enacted; the law of 2003 it replaced is not included. The Ley General de Bibliotecas of 2021 starts as enacted; the law of 1988 it replaced is not included. The Ley para Regular las Agrupaciones Financieras of 2014 starts as enacted, from its own file name; the law of 1990 it replaced is not included. The Ley de Carrera Judicial del Poder Judicial de la Federación of 2025 took the file name of the law of 2021 it abrogated; the 2021 law is not included.
- **Credits in the Código Fiscal de la Federación.** The Cámara marks few of its paragraphs with reform notes, so most of its changes are unexplained (publisher) commits, dated when every decree between the two copies compared is in force.
- **Staggered and gradual starts.** The CNPP entered into force gradually by declaratorias (at the latest 18 June 2016) and is dated by the default rule; the CNPCF applies gradually by declaratorias (at the latest 1 April 2027), and the decree that issued it abrogates the Código Federal de Procedimientos Civiles on the same schedule. Neither schedule is modelled.
- **One-unit act.** The Cámara de Diputados prints the tax on services declared of public interest (DOF 31-12-1968, artículo Noveno of a law that amended several taxes) with its articles inside quotation marks, so `ley-del-impuesto-sobre-servicios-de-interes-publico/` keeps the whole text as one file; it is dated 1 July 1969, the day that law's artículo Cuarto transitorio puts this tax in force.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

`reforms.py` reads the Cámara's chronological list of reforms; the parsers Lexifina's code (Constitution), Lexifina's code (LFPDPPP) and Lexifina's code (the codes and laws) turn the archived copies into the corpus; the shared builder `tools/build.py` writes the history with `git fast-import`.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Leyes Federales Vigentes, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/) | Official legislation | current text only, plus each decree as published | yes, a note per paragraph from 2013, and a chronological list of reforms | no | Used, in archived copies: `pdf/<n>.pdf`, `pdf/<n>_<date>.pdf` and `pdf/<CODE>.pdf` for each act, and each act's reform list `ref/<code>.htm` (`ref/cpeum_crono.htm` for the Constitution) |
| [Internet Archive Wayback Machine](https://web.archive.org/) | Archive | yes, by capture | n/a | n/a | Most copies used; each pinned by its capture timestamp |
| – | Archives | yes, by capture | n/a | n/a | A few copies used (named in `REPRODUCE.md`), each pinned by its capture |
| [Diario Oficial de la Federación](https://www.dof.gob.mx/) | Official gazette | n/a | n/a | no | Not read; the Cámara gives the DOF date of every decree |
| [SCJN Legislación](https://legislacion.scjn.gob.mx/) | Official legislation | possibly | possibly | no | Not explored |
| [lex-mx](https://github.com/ingteranalvarez/lex-mx) | Volunteer git repo | current text, daily since 2026 | partly | n/a | Prior art; no text copied |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of the United Mexican States, as consolidated by the Cámara de Diputados del H. The Ley Federal del Derecho de Autor, art. 14, fracción VIII, excludes legislative texts from copyright protection. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## En español

Historia del derecho mexicano en git: un archivo por disposición y un commit por decreto, fechado el día de su entrada en vigor y firmado por el decreto que hizo el cambio (`git blame` nombra el decreto de cada párrafo). Contiene la Constitución Política de los Estados Unidos Mexicanos desde el texto vigente el 8 de abril de 2006 (la copia más antigua disponible) hasta la reforma publicada en el DOF el 7 de octubre de 2026: las reformas 167 a 285. Contiene también la Ley Federal de Protección de Datos Personales en Posesión de los Particulares: la ley de 2010 tal como se publicó, la nueva ley del mismo nombre (DOF 20-03-2025) que la abrogó, y su reforma del 14 de noviembre de 2025. Contiene además los códigos Civil Federal, Penal Federal, de Comercio, Federal de Procedimientos Civiles, Fiscal de la Federación, Nacional de Procedimientos Penales y Nacional de Procedimientos Civiles y Familiares, y las leyes Federal del Trabajo, de Amparo, General de Sociedades Mercantiles, General de Títulos y Operaciones de Crédito, de Instituciones de Crédito, Federal de Protección al Consumidor, de Concursos Mercantiles, del Mercado de Valores y del Seguro Social, cada uno desde la copia consolidada más antigua disponible (o desde su publicación original) hasta su última reforma.

- Texto vigente en una fecha: `python tools/en_vigor_el.py 2020-01-01 constitucion 82`
- Fechas: las del primer artículo transitorio de cada decreto; regla supletoria, art. 3 del Código Civil Federal (tres días después de su publicación).
- Autoría: cada cambio se atribuye a un decreto solo si una nota de la Cámara ("Párrafo reformado DOF …") da su fecha; lo que ninguna nota explica queda como "unexplained", a nombre de la Cámara de Diputados.
- Fuente: Cámara de Diputados del H. Ningún modelo de IA escribió texto legal.
