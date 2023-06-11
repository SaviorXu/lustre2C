/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:01:33
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_le_lustre_logic.h"

/* lustre_logic::lustre_le/ */
void lustre_le_lustre_logic(
  inC_lustre_le_lustre_logic *inC,
  outC_lustre_le_lustre_logic *outC)
{
  outC->out_Z = inC->in_X <= inC->in_Y;
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_le_init_lustre_logic(outC_lustre_le_lustre_logic *outC)
{
  outC->out_Z = kcg_true;
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_le_reset_lustre_logic(outC_lustre_le_lustre_logic *outC)
{
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_le_lustre_logic.c
** Generation date: 2022-06-09T22:01:33
*************************************************************$ */

