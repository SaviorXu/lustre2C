/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:03:53
*************************************************************$ */
#ifndef _lustre_init_lustre_time_H_
#define _lustre_init_lustre_time_H_

#include "kcg_types.h"

/* ========================  input structure  ====================== */
typedef struct { kcg_int8 /* _L3/, in_X/ */ in_X; } inC_lustre_init_lustre_time;

/* =====================  no output structure  ====================== */

/* ========================  context type  ========================= */
typedef struct {
  /* ---------------------------  outputs  --------------------------- */
  kcg_int8 /* _L1/, out_Y/ */ out_Y;
  /* -----------------------  no local probes  ----------------------- */
  /* ----------------------- local memories  ------------------------- */
  kcg_bool init;
  /* -------------------- no sub nodes' contexts  -------------------- */
  /* ----------------- no clocks of observable data ------------------ */
} outC_lustre_init_lustre_time;

/* ===========  node initialization and cycle functions  =========== */
/* lustre_time::lustre_init/ */
extern void lustre_init_lustre_time(
  inC_lustre_init_lustre_time *inC,
  outC_lustre_init_lustre_time *outC);

#ifndef KCG_NO_EXTERN_CALL_TO_RESET
extern void lustre_init_reset_lustre_time(outC_lustre_init_lustre_time *outC);
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */

#ifndef KCG_USER_DEFINED_INIT
extern void lustre_init_init_lustre_time(outC_lustre_init_lustre_time *outC);
#endif /* KCG_USER_DEFINED_INIT */



#endif /* _lustre_init_lustre_time_H_ */
/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_init_lustre_time.h
** Generation date: 2022-06-09T22:03:53
*************************************************************$ */

