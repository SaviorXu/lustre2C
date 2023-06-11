/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:03:40
*************************************************************$ */
#ifndef _lustre_fby_lustre_time_H_
#define _lustre_fby_lustre_time_H_

#include "kcg_types.h"

/* ========================  input structure  ====================== */
typedef struct { kcg_int8 /* in_X/ */ in_X; } inC_lustre_fby_lustre_time;

/* =====================  no output structure  ====================== */

/* ========================  context type  ========================= */
typedef struct {
  /* ---------------------------  outputs  --------------------------- */
  kcg_int8 /* _L1/, out_Y/ */ out_Y;
  /* -----------------------  no local probes  ----------------------- */
  /* ----------------------- local memories  ------------------------- */
  kcg_int8 /* _L2/ */ _L2;
  /* -------------------- no sub nodes' contexts  -------------------- */
  /* ----------------- no clocks of observable data ------------------ */
} outC_lustre_fby_lustre_time;

/* ===========  node initialization and cycle functions  =========== */
/* lustre_time::lustre_fby/ */
extern void lustre_fby_lustre_time(
  inC_lustre_fby_lustre_time *inC,
  outC_lustre_fby_lustre_time *outC);

#ifndef KCG_NO_EXTERN_CALL_TO_RESET
extern void lustre_fby_reset_lustre_time(outC_lustre_fby_lustre_time *outC);
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */

#ifndef KCG_USER_DEFINED_INIT
extern void lustre_fby_init_lustre_time(outC_lustre_fby_lustre_time *outC);
#endif /* KCG_USER_DEFINED_INIT */



#endif /* _lustre_fby_lustre_time_H_ */
/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_fby_lustre_time.h
** Generation date: 2022-06-09T22:03:40
*************************************************************$ */

