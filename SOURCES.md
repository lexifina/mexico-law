# Sources and legal basis

## Used
- **Suprema Corte de Justicia de la Nación, "Legislación"** (https://legislacion.scjn.gob.mx). For each federal law:
  the list of its DOF publications (wfOrdenamientoDetalle), the "texto completo" Word file of each publication
  (AbrirDocArticulo: the whole consolidated text after it, headed "ÚLTIMA REFORMA PUBLICADA EN EL DIARIO OFICIAL DE
  LA FEDERACIÓN: <date>") and its extracto (wfExtracto: SCJN's summary of the decree, quoting its transitorios).
  SCJN says: "La edición de los ordenamientos jurídicos del ámbito federal en medios electrónicos representa una
  versión oficial, con base en lo dispuesto por los artículos 2°, 5°, 6° fracción IV, y 8° de la Ley del Diario
  Oficial de la Federación y Gacetas Gubernamentales."
- robots.txt: legislacion.scjn.gob.mx has none (404); www.scjn.gob.mx's names no AI agent and does not cover these
  paths.
- Terms: https://www.scjn.gob.mx/terminos-condiciones (section 4: copying allowed "con fines exclusivamente
  informativos, académicos, de orientación"; no commercialising; section 7: cite the location and the date of
  consultation). No clause forbids automated access.
- Copyright: Ley Federal del Derecho de Autor, art. 14, fr. VIII: legislative texts are not protected.

## Not used, and why
- **Cámara de Diputados, Leyes Federales Vigentes** (www.diputados.gob.mx/LeyesBiblio): not reachable from the
  build machine (TCP connections to 201.147.98.82 on ports 80 and 443 time out, 2026-10-28).
- **Diario Oficial de la Federación** (dof.gob.mx): its robots.txt disallows `/nota_detalle.php?` (every decree
  page) and `/nota_to_doc.php?` for all agents.
- **Orden Jurídico Nacional** (ordenjuridico.gob.mx, SEGOB): current text only, and behind (its Constitution is of
  15-04-2025).

## Request log
1895 requests to legislacion.scjn.gob.mx between 2026-10-28T22:56:28 and 2026-10-29T00:22:48, one process, at most 3 at a
time with a 0.6 s pause before each; every answer cached.
