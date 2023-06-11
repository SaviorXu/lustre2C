/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:03:40
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_fby_lustre_time.h"

/* lustre_time::lustre_fby/ */
void lustre_fby_lustre_time(
  inC_lustre_fby_lustre_time *inC,
  outC_lustre_fby_lustre_time *outC)
{
  outC->out_Y = outC->_L2;
  outC->_L2 = inC->in_X;
}

#ifndef KCG_USER_DEFINED_INIT
void lustre_fby_init_lustre_time(outC_lustre_fby_lustre_time *outC)
{
  outC->out_Y = kcg_lit_int8(0);
  outC->_L2 = init_V_lustre_time;
}
#endif /* KCG_USER_DEFINED_INIT */


#ifndef KCG_NO_EXTERN_CALL_TO_RESET
void lustre_fby_reset_lustre_time(outC_lustre_fby_lustre_time *outC)
{
  outC->_L2 = init_V_lustre_time;
}
#endif /* KCG_NO_EXTERN_CALL_TO_RESET */



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_fby_lustre_time.c
** Generation date: 2022-06-09T22:03:40
*************************************************************$ */

