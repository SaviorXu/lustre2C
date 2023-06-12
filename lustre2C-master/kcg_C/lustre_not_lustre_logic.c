/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:01:56
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_not_lustre_logic.h"

/* lustre_logic::lustre_not/ */
void lustre_not_lustre_logic(
  inC_lustre_not_lustre_logic *inC,
  outC_lustre_not_lustre_logic *outC)
{
  outC->out_Y = !inC->in_X;
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_not_init_lustre_logic(outC_lustre_not_lustre_logic *outC)
{
  outC->out_Y = kcg_true;
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_not_reset_lustre_logic(outC_lustre_not_lustre_logic *outC)
{
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_not_lustre_logic.c
** Generation date: 2022-06-09T22:01:56
*************************************************************$ */

