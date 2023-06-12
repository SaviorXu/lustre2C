/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T21:59:43
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_and_lustre_logic.h"

/* lustre_logic::lustre_and/ */
void lustre_and_lustre_logic(
  inC_lustre_and_lustre_logic *inC,
  outC_lustre_and_lustre_logic *outC)
{
  outC->out_Z = inC->in_X & inC->in_Y;
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_and_init_lustre_logic(outC_lustre_and_lustre_logic *outC)
{
  outC->out_Z = kcg_true;
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_and_reset_lustre_logic(outC_lustre_and_lustre_logic *outC)
{
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_and_lustre_logic.c
** Generation date: 2022-06-09T21:59:43
*************************************************************$ */

