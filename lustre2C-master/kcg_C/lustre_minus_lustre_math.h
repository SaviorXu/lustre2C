/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:02:19
*************************************************************$ */
#ifndef _lustre_minus_lustre_math_H_
#define _lustre_minus_lustre_math_H_

#include "kcg_types.h"

/* ========================  input structure  ====================== */
typedef struct {
  kcg_int8 /* _L2/, in_X/ */ in_X;
  kcg_int8 /* _L3/, in_Y/ */ in_Y;
} inC_lustre_minus_lustre_math;

/* =====================  no output structure  ====================== */

/* ========================  context type  ========================= */
typedef struct {
  /* ---------------------------  outputs  --------------------------- */
  kcg_int8 /* _L1/, out_Z/ */ out_Z;
  /* -----------------------  no local probes  ----------------------- */
  /* -----------------------  no local memory  ----------------------- */
  /* -------------------- no sub nodes' contexts  -------------------- */
  /* ----------------- no clocks of observable data ------------------ */
} outC_lustre_minus_lustre_math;

/* ===========  node initialization and cycle functions  =========== */
/* lustre_math::lustre_minus/ */
extern void lustre_minus_lustre_math(
  inC_lustre_minus_lustre_math *inC,
  outC_lustre_minus_lustre_math *outC);

#ifndef KCG_NO_EXTERN_CALL_TO_RESET
extern void lustre_minus_reset_lustre_math(outC_lustre_minus_lustre_math *outC);
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */

#ifndef KCG_USER_DEFINED_INIT
extern void lustre_minus_init_lustre_math(outC_lustre_minus_lustre_math *outC);
#endif /* KCG_USER_DEFINED_INIT */



#endif /* _lustre_minus_lustre_math_H_ */
/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_minus_lustre_math.h
** Generation date: 2022-06-09T22:02:19
*************************************************************$ */

