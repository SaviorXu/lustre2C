/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:02:31
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_plus_lustre_math.h"

/* lustre_math::lustre_plus/ */
void lustre_plus_lustre_math(
  inC_lustre_plus_lustre_math *inC,
  outC_lustre_plus_lustre_math *outC)
{
  outC->out_Z = inC->in_X + inC->in_Y;
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_plus_init_lustre_math(outC_lustre_plus_lustre_math *outC)
{
  outC->out_Z = kcg_lit_int8(0);
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_plus_reset_lustre_math(outC_lustre_plus_lustre_math *outC)
{
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_plus_lustre_math.c
** Generation date: 2022-06-09T22:02:31
*************************************************************$ */

