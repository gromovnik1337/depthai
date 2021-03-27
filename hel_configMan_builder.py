config = {
            # Possible streams:
            # ['left', 'right', 'jpegout', 'video', 'previewout', 'metaout', 'depth_sipp', 'disparity', 'depth_color_h']
            # If "left" is used, it must be in the first position.
            # To test depth use:
            # 'streams': [{'name': 'depth_sipp', "max_fps": 12.0}, {'name': 'previewout', "max_fps": 12.0}, ],
            'streams': ['metaout','previewout'],
            'depth':
            {
                'calibration_file': '',
                'left_mesh_file': '/home/alex/Alex/Aicomp/HELIOS/depthai/resources/mesh_left.calib',
                'right_mesh_file': '/home/alex/Alex/Aicomp/HELIOS/depthai/resources/mesh_right.calib',
                'padding_factor': 0.3,
                'depth_limit_m': 10.0, # In meters, for filtering purpose during x,y,z calc
                'median_kernel_size': 7,
                'lr_check': False,
                'warp_rectify':
                {
                    'use_mesh' : False, # if False, will use homography
                    'mirror_frame': True, # if False, the disparity will be mirrored instead
                    'edge_fill_color': 0, # gray 0..255, or -1 to replicate pixel values
                },
            },
            'ai':
            {
                'blob_file': '/home/alex/Alex/Aicomp/HELIOS/depthai/resources/nn/human-pose-estimation-0001/human-pose-estimation-0001.blob.sh14cmx14NCE1',
                'blob_file_config': '/home/alex/Alex/Aicomp/HELIOS/depthai/resources/nn/human-pose-estimation-0001/human-pose-estimation-0001.json',
                'blob_file2': '',
                'blob_file_config2': '',
                'calc_dist_to_bb': False,
                'keep_aspect_ratio': False,
                'camera_input': 'rgb',
                'shaves' : 14,
                'cmx_slices' : 14,
                'NN_engines' : 1,
            },
            # object tracker
            'ot':
            {
                'max_tracklets'        : 20, #maximum 20 is supported
                'confidence_threshold' : 0.5, #object is tracked only for detections over this threshold
            },
            'board_config':
            {
                'swap_left_and_right_cameras': True, # True for 1097 (RPi Compute) and 1098OBC (USB w/onboard cameras)
                'left_fov_deg': 71.86, # Same on 1097 and 1098OBC
                'rgb_fov_deg': 68.7938,
                'left_to_right_distance_cm': 7.5, # Distance between stereo cameras
                'left_to_rgb_distance_cm': 3.5, # Currently unused
                'store_to_eeprom': False,
                'clear_eeprom': False,
                'override_eeprom': False,
            },
            'camera':
            {
                'rgb':
                {
                    # 3840x2160, 1920x1080
                    # only UHD/1080p/30 fps supported for now
                    'resolution_h': 1080,
                    'fps': 30.0,
                },
                'mono':
                {
                    # 1280x720, 1280x800, 640x400 (binning enabled)
                    'resolution_h': 400,
                    'fps': 30.0,
                },
            },
            'app':
            {
                'sync_video_meta_streams': False,
                'sync_sequence_numbers'  : False,
                'usb_chunk_KiB' : 64,
            },
            #'video_config':
            #{
            #    'rateCtrlMode': 'cbr', # Options: cbr / vbr
            #    'profile': 'h265_main', # Options: 'h264_baseline' / 'h264_main' / 'h264_high' / 'h265_main / 'mjpeg' '
            #    'bitrate': 8000000, # When using CBR (H264/H265 only)
            #    'maxBitrate': 8000000, # When using CBR (H264/H265 only)
            #    'keyframeFrequency': 30, (H264/H265 only)
            #    'numBFrames': 0, (H264/H265 only)
            #    'quality': 80 # (0 - 100%) When using VBR or MJPEG profile
            #}
            #'video_config':
            #{
            #    'profile': 'mjpeg',
            #    'quality': 95
            #}
        }