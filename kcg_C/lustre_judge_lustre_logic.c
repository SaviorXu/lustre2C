/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:01:23
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_judge_lustre_logic.h"

/* lustre_logic::lustre_judge/ */
void lustre_judge_lustre_logic(
  inC_lustre_judge_lustre_logic *inC,
  outC_lustre_judge_lustre_logic *outC)
{
  outC->out_Z = /* _L1=(lustre_logic::lustre_if#1)/ */
    lustre_if_lustre_logic(
      inC->in_X,
      inC->in_Y,
      /* _L6=(lustre_logic::lustre_le#1)/ */
      lustre_le_lustre_logic(inC->in_C1, inC->in_C2));
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_judge_init_lustre_logic(outC_lustre_judge_lustre_logic *outC)
{
  outC->out_Z = kcg_lit_int8(0);
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_judge_reset_lustre_logic(outC_lustre_judge_lustre_logic *outC)
{
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_judge_lustre_logic.c
** Generation date: 2022-06-09T22:01:23
*************************************************************$ */

