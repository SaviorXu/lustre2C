/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:03:53
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_init_lustre_time.h"

/* lustre_time::lustre_init/ */
void lustre_init_lustre_time(
  inC_lustre_init_lustre_time *inC,
  outC_lustre_init_lustre_time *outC)
{
  /* _L1= */
  if (outC->init) {
    outC->init = kcg_false;
    outC->out_Y = init_V_lustre_time;
  }
  else {
    outC->out_Y = inC->in_X;
  }
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_init_init_lustre_time(outC_lustre_init_lustre_time *outC)
{
  outC->init = kcg_true;
  outC->out_Y = kcg_lit_int8(0);
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_init_reset_lustre_time(outC_lustre_init_lustre_time *outC)
{
  outC->init = kcg_true;
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_init_lustre_time.c
** Generation date: 2022-06-09T22:03:53
*************************************************************$ */

