/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:01:56
*************************************************************$ */
#ifndef _lustre_not_lustre_logic_H_
#define _lustre_not_lustre_logic_H_

#include "kcg_types.h"

/* ========================  input structure  ====================== */
typedef struct { kcg_bool /* _L5/, in_X/ */ in_X; } inC_lustre_not_lustre_logic;

/* =====================  no output structure  ====================== */

/* ========================  context type  ========================= */
typedef struct {
  /* ---------------------------  outputs  --------------------------- */
  kcg_bool /* _L8/, out_Y/ */ out_Y;
  /* -----------------------  no local probes  ----------------------- */
  /* -----------------------  no local memory  ----------------------- */
  /* -------------------- no sub nodes' contexts  -------------------- */
  /* ----------------- no clocks of observable data ------------------ */
} outC_lustre_not_lustre_logic;

/* ===========  node initialization and cycle functions  =========== */
/* lustre_logic::lustre_not/ */
extern void lustre_not_lustre_logic(
  inC_lustre_not_lustre_logic *inC,
  outC_lustre_not_lustre_logic *outC);

#ifndef KCG_NO_EXTERN_CALL_TO_RESET
extern void lustre_not_reset_lustre_logic(outC_lustre_not_lustre_logic *outC);
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */

#ifndef KCG_USER_DEFINED_INIT
extern void lustre_not_init_lustre_logic(outC_lustre_not_lustre_logic *outC);
#endif /* KCG_USER_DEFINED_INIT */



#endif /* _lustre_not_lustre_logic_H_ */
/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_not_lustre_logic.h
** Generation date: 2022-06-09T22:01:56
*************************************************************$ */

