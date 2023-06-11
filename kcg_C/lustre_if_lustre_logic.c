/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** Command: kcg661.exe -config D:/test123/KCG/config.txt
** Generation date: 2022-06-09T22:01:23
*************************************************************$ */

#include "kcg_consts.h"
#include "kcg_sensors.h"
#include "lustre_if_lustre_logic.h"

/* lustre_logic::lustre_if/ */
kcg_int8 lustre_if_lustre_logic(
  /* _L2/, in_X/ */
  kcg_int8 in_X,
  /* _L3/, in_Y/ */
  kcg_int8 in_Y,
  /* _L4/, in_judge/ */
  kcg_bool in_judge)
{
  /* _L1/, out_Z/ */
  kcg_int8 out_Z;

  /* _L1= */
  if (in_judge) {
    out_Z = in_X;
  }
  else {
    out_Z = in_Y;
  }
  return out_Z;
}



/* $******* SCADE Suite KCG 32-bit 6.6.1 beta (build i1) ********
** lustre_if_lustre_logic.c
** Generation date: 2022-06-09T22:01:23
*************************************************************$ */

