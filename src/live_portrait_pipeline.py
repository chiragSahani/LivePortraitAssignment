import concurrent.futures

if inf_cfg.flag_pasteback and inf_cfg.flag_do_crop and inf_cfg.flag_stitching:
    # Parallelize paste_back for video
    if flag_is_source_video and I_p_pstbk_lst is not None and len(I_p_lst) > 1:
        def paste_back_args(args):
            I_p_i, M_c2o, rgb, mask = args
            return paste_back(I_p_i, M_c2o, rgb, mask)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            I_p_pstbk_lst = list(executor.map(
                paste_back_args,
                zip(I_p_lst, source_M_c2o_lst, source_rgb_lst, [mask_ori_float]*len(I_p_lst))
            ))
    else:
        for i in range(len(I_p_lst)):
            if flag_is_source_video:
                I_p_pstbk = paste_back(I_p_lst[i], source_M_c2o_lst[i], source_rgb_lst[i], mask_ori_float)
            else:
                I_p_pstbk = paste_back(I_p_lst[i], crop_info['M_c2o'], source_rgb_lst[0], mask_ori_float)
            I_p_pstbk_lst.append(I_p_pstbk) 