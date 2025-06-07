# Features order: trip_duration_days, miles_traveled, total_receipts_amount, miles_per_day, spend_per_day, miles_bucket, receipts_bucket, miles_per_day_bucket, receipt_cents, spend_per_day_bucket
def score(input):
    if input[0] < 3.0:
        var0 = 5.0
    else:
        var0 = 21.683332
    if input[0] < 3.0:
        var1 = 5.3333335
    else:
        var1 = 20.237778
    if input[0] < 3.0:
        var2 = 4.9777775
    else:
        var2 = 18.888594
    if input[0] < 2.0:
        var3 = 2.7344444
    else:
        var3 = 17.629354
    if input[0] < 2.0:
        var4 = 2.5977223
    else:
        var4 = 16.454062
    if input[0] < 3.0:
        var5 = 3.332073
    else:
        var5 = 15.357124
    if input[0] < 5.0:
        var6 = 4.588695
    else:
        var6 = 16.987488
    if input[0] < 5.0:
        var7 = 4.283053
    else:
        var7 = 16.138113
    if input[0] < 5.0:
        var8 = 3.9233139
    else:
        var8 = 15.331207
    if input[0] < 5.0:
        var9 = 3.8727345
    else:
        var9 = 14.564647
    if input[0] < 5.0:
        var10 = 3.3386102
    else:
        var10 = 13.836413
    if input[0] < 5.0:
        var11 = 3.0882146
    else:
        var11 = 13.144594
    if input[0] < 5.0:
        var12 = 2.8565986
    else:
        var12 = 12.487365
    if input[0] < 5.0:
        var13 = 2.854024
    else:
        var13 = 11.862996
    if input[0] < 3.0:
        var14 = 1.1895854
    else:
        var14 = 9.561381
    if input[0] < 5.0:
        var15 = 2.3053901
    else:
        var15 = 10.791778
    if input[1] < 500.0:
        var16 = 2.1516976
    else:
        var16 = 10.252189
    if input[0] < 5.0:
        if input[0] < 3.0:
            var17 = 0.8131406
        else:
            var17 = 2.3713021
    else:
        var17 = 9.739579
    if input[0] < 5.0:
        if input[0] < 3.0:
            var18 = 0.6004173
        else:
            var18 = 2.2527368
    else:
        var18 = 9.252601
    if input[0] < 5.0:
        if input[0] < 3.0:
            var19 = 0.71890336
        else:
            var19 = 2.1401002
    else:
        var19 = 8.78997
    if input[0] < 5.0:
        if input[0] < 3.0:
            var20 = 0.6709765
        else:
            var20 = 2.033095
    else:
        var20 = 8.3504715
    if input[0] < 5.0:
        if input[0] < 3.0:
            var21 = 0.6262449
        else:
            var21 = 1.93144
    else:
        var21 = 7.9329486
    if input[0] < 5.0:
        if input[0] < 3.0:
            var22 = 0.5844953
        else:
            var22 = 1.8348678
    else:
        var22 = 7.5363007
    if input[0] < 5.0:
        if input[0] < 3.0:
            var23 = 0.54552895
        else:
            var23 = 1.7431244
    else:
        var23 = 7.159485
    if input[0] < 5.0:
        if input[0] < 3.0:
            var24 = 0.413089
        else:
            var24 = 1.6559685
    else:
        var24 = 6.801511
    var25 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24
    if input[0] < 5.0:
        if input[0] < 3.0:
            var26 = 0.48162103
        else:
            var26 = 1.5731697
    else:
        var26 = 6.461435
    if input[0] < 5.0:
        if input[0] < 2.0:
            var27 = 0.30591583
        else:
            var27 = 1.4945115
    else:
        var27 = 6.138364
    if input[0] < 5.0:
        if input[0] < 3.0:
            var28 = 0.29362795
        else:
            var28 = 1.4197861
    else:
        var28 = 5.831445
    if input[0] < 5.0:
        if input[0] < 3.0:
            var29 = 0.36992368
        else:
            var29 = 1.3487968
    else:
        var29 = 5.5398726
    if input[2] < 300.0:
        if input[2] < 150.75:
            var30 = 0.3452619
        else:
            var30 = 1.2813568
    else:
        var30 = 5.2628784
    if input[0] < 5.0:
        if input[0] < 3.0:
            var31 = 0.32224452
        else:
            var31 = 1.217289
    else:
        var31 = 4.9997344
    if input[0] < 5.0:
        if input[0] < 3.0:
            var32 = 0.30076167
        else:
            var32 = 1.1564248
    else:
        var32 = 4.749748
    if input[0] < 5.0:
        if input[0] < 3.0:
            var33 = 0.2807111
        else:
            var33 = 1.0986038
    else:
        var33 = 4.5122604
    if input[0] < 5.0:
        if input[0] < 3.0:
            var34 = 0.26199722
        else:
            var34 = 1.0436738
    else:
        var34 = 4.2866473
    if input[0] < 5.0:
        if input[0] < 2.0:
            var35 = 0.18189393
        else:
            var35 = 0.9914902
    else:
        var35 = 4.0723147
    if input[0] < 5.0:
        if input[0] < 3.0:
            var36 = 0.13532753
        else:
            var36 = 0.9419159
    else:
        var36 = 3.8686981
    if input[0] < 5.0:
        if input[0] < 3.0:
            var37 = 0.12856102
        else:
            var37 = 0.8948204
    else:
        var37 = 3.6752625
    if input[0] < 5.0:
        if input[0] < 3.0:
            var38 = 0.122132875
        else:
            var38 = 0.85007936
    else:
        var38 = 3.4914994
    if input[0] < 5.0:
        if input[0] < 3.0:
            var39 = 0.17968293
        else:
            var39 = 0.8075752
    else:
        var39 = 3.316925
    if input[0] < 5.0:
        if input[0] < 2.0:
            var40 = 0.14451408
        else:
            var40 = 0.76719666
    else:
        var40 = 3.151079
    if input[1] < 500.0:
        if input[1] < 50.0:
            var41 = 0.068682484
        else:
            var41 = 0.72883683
    else:
        var41 = 2.9935243
    if input[0] < 5.0:
        if input[0] < 3.0:
            var42 = 0.110729985
        else:
            var42 = 0.69239503
    else:
        var42 = 2.8438478
    if input[1] < 500.0:
        if input[1] < 180.0:
            var43 = 0.10334778
        else:
            var43 = 0.6577751
    else:
        var43 = 2.7016556
    if input[0] < 5.0:
        if input[0] < 3.0:
            var44 = 0.05454445
        else:
            var44 = 0.62488633
    else:
        var44 = 2.5665727
    if input[0] < 5.0:
        if input[0] < 3.0:
            var45 = 0.09282176
        else:
            var45 = 0.5936417
    else:
        var45 = 2.4382446
    if input[0] < 5.0:
        if input[0] < 3.0:
            var46 = 0.04717636
        else:
            var46 = 0.56395954
    else:
        var46 = 2.316333
    if input[0] < 5.0:
        if input[0] < 3.0:
            var47 = 0.083488464
        else:
            var47 = 0.5357613
    else:
        var47 = 2.2005157
    if input[2] < 300.0:
        if input[2] < 60.0:
            var48 = 0.07624092
        else:
            var48 = 0.50897294
    else:
        var48 = 2.0904908
    if input[2] < 300.0:
        if input[2] < 150.75:
            if input[2] < 60.0:
                var49 = 0.0724289
            else:
                var49 = 0.015194321
        else:
            var49 = 0.48352432
    else:
        var49 = 1.9859666
    if input[0] < 5.0:
        if input[0] < 3.0:
            var50 = 0.014434434
        else:
            var50 = 0.4593483
    else:
        var50 = 1.8866684
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var51 = 0.068085864
            else:
                var51 = 0.013712692
        else:
            var51 = 0.43638077
    else:
        var51 = 1.7923355
    if input[0] < 5.0:
        if input[0] < 2.0:
            var52 = 0.06468163
        else:
            var52 = 0.41456148
    else:
        var52 = 1.7027191
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var53 = 0.061447527
            else:
                var53 = -0.0077007296
        else:
            var53 = 0.39383316
    else:
        var53 = 1.6175827
    if input[0] < 5.0:
        var54 = 0.3741417
    else:
        var54 = 1.5367035
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var55 = 0.039668273
            else:
                var55 = -0.026023103
        else:
            var55 = 0.35543442
    else:
        var55 = 1.4598678
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var56 = 0.037685014
            else:
                var56 = -0.02472191
        else:
            var56 = 0.33766252
    else:
        var56 = 1.3868744
    if input[0] < 5.0:
        if input[0] < 3.0:
            var57 = -0.023485947
        else:
            var57 = 0.3207794
    else:
        var57 = 1.3175309
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var58 = 0.036975097
            else:
                var58 = -0.022311782
        else:
            var58 = 0.30474016
    else:
        var58 = 1.251654
    if input[1] < 500.0:
        if input[1] < 180.0:
            if input[1] < 50.0:
                var59 = -0.021196365
            else:
                var59 = 0.035126496
        else:
            var59 = 0.28950348
    else:
        var59 = 1.1890717
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var60 = 0.033370208
            else:
                var60 = -0.020136643
        else:
            var60 = 0.27502823
    else:
        var60 = 1.1296173
    if input[0] < 5.0:
        if input[0] < 3.0:
            var61 = -0.019129945
        else:
            var61 = 0.26127702
    else:
        var61 = 1.0731369
    if input[0] < 5.0:
        if input[0] < 3.0:
            var62 = -0.0181736
        else:
            var62 = 0.2482132
    else:
        var62 = 1.0194794
    if input[0] < 5.0:
        if input[0] < 3.0:
            var63 = -0.017264938
        else:
            var63 = 0.23580246
    else:
        var63 = 0.96850586
    if input[1] < 500.0:
        if input[1] < 50.0:
            var64 = -0.016401673
        else:
            var64 = 0.224012
    else:
        var64 = 0.9200806
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var65 = 0.023229217
            else:
                var65 = -0.015581513
        else:
            var65 = 0.21281128
    else:
        var65 = 0.87407684
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var66 = 0.022067642
            else:
                var66 = -0.014802552
        else:
            var66 = 0.20217057
    else:
        var66 = 0.83037263
    if input[0] < 5.0:
        if input[0] < 3.0:
            var67 = -0.014062501
        else:
            var67 = 0.19206238
    else:
        var67 = 0.78885347
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var68 = 0.02166748
            else:
                var68 = -0.013359452
        else:
            var68 = 0.18245926
    else:
        var68 = 0.74941105
    if input[0] < 5.0:
        if input[0] < 3.0:
            if input[0] < 2.0:
                var69 = 0.020584106
            else:
                var69 = -0.012691498
        else:
            var69 = 0.17333603
    else:
        var69 = 0.71194
    if input[0] < 5.0:
        if input[0] < 2.0:
            var70 = 0.019554902
        else:
            var70 = 0.16466904
    else:
        var70 = 0.6763428
    if input[0] < 3.0:
        if input[0] < 2.0:
            var71 = 0.018577194
        else:
            var71 = -0.020290375
    else:
        if input[0] < 5.0:
            var71 = 0.1564354
        else:
            var71 = 0.64252627
    if input[1] < 500.0:
        if input[1] < 180.0:
            var72 = 0.017648315
        else:
            var72 = 0.14861374
    else:
        var72 = 0.6104004
    if input[1] < 500.0:
        if input[1] < 180.0:
            var73 = 0.016765976
        else:
            var73 = 0.1411827
    else:
        var73 = 0.57987976
    if input[0] < 3.0:
        var74 = -0.020996476
    else:
        if input[0] < 5.0:
            var74 = 0.13412324
        else:
            var74 = 0.550885
    if input[0] < 5.0:
        if input[0] < 2.0:
            var75 = 0.01697731
        else:
            var75 = 0.127417
    else:
        var75 = 0.52334136
    if input[0] < 3.0:
        if input[0] < 2.0:
            var76 = 0.01612854
        else:
            var76 = -0.026317596
    else:
        if input[0] < 5.0:
            var76 = 0.121046446
        else:
            var76 = 0.49717408
    if input[0] < 3.0:
        var77 = -0.025001526
    else:
        if input[0] < 5.0:
            var77 = 0.11499405
        else:
            var77 = 0.472316
    if input[1] < 180.0:
        if input[1] < 50.0:
            var78 = -0.02375145
        else:
            var78 = 0.01657219
    else:
        if input[1] < 500.0:
            var78 = 0.10924454
        else:
            var78 = 0.44869995
    if input[0] < 3.0:
        if input[0] < 2.0:
            var79 = 0.015743637
        else:
            var79 = -0.022563934
    else:
        if input[0] < 5.0:
            var79 = 0.103782654
        else:
            var79 = 0.42626497
    if input[0] < 3.0:
        if input[0] < 2.0:
            var80 = 0.014956283
        else:
            var80 = -0.021435548
    else:
        if input[0] < 5.0:
            var80 = 0.09859314
        else:
            var80 = 0.40495148
    var81 = var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80
    if input[0] < 3.0:
        if input[0] < 2.0:
            var82 = 0.014208603
        else:
            var82 = -0.020363618
    else:
        if input[0] < 5.0:
            var82 = 0.09366379
        else:
            var82 = 0.3847046
    if input[0] < 3.0:
        if input[0] < 2.0:
            var83 = 0.013498306
        else:
            var83 = -0.019345475
    else:
        if input[0] < 5.0:
            var83 = 0.08898087
        else:
            var83 = 0.36546937
    if input[0] < 3.0:
        var84 = -0.018378068
    else:
        if input[0] < 5.0:
            var84 = 0.084532164
        else:
            var84 = 0.34719545
    if input[0] < 3.0:
        if input[0] < 2.0:
            var85 = 0.013742447
        else:
            var85 = -0.017459108
    else:
        if input[0] < 5.0:
            var85 = 0.08030548
        else:
            var85 = 0.3298355
    if input[0] < 3.0:
        if input[0] < 2.0:
            var86 = 0.0130554205
        else:
            var86 = -0.016586304
    else:
        if input[0] < 5.0:
            var86 = 0.07629013
        else:
            var86 = 0.31334382
    if input[0] < 5.0:
        if input[0] < 2.0:
            var87 = 0.012402725
        else:
            var87 = 0.07247543
    else:
        var87 = 0.2976761
    if input[0] < 3.0:
        if input[0] < 2.0:
            var88 = 0.011782455
        else:
            var88 = -0.019380951
    else:
        if input[0] < 5.0:
            var88 = 0.06885147
        else:
            var88 = 0.28279266
    if input[0] < 5.0:
        if input[0] < 2.0:
            var89 = 0.011193466
        else:
            var89 = 0.06540909
    else:
        var89 = 0.26865235
    if input[0] < 5.0:
        var90 = 0.062138367
    else:
        var90 = 0.25522003
    if input[0] < 3.0:
        if input[0] < 2.0:
            var91 = 0.007526779
        else:
            var91 = -0.024789428
    else:
        if input[0] < 5.0:
            var91 = 0.059031677
        else:
            var91 = 0.2424591
    if input[1] < 50.0:
        var92 = -0.023550034
    else:
        if input[1] < 500.0:
            var92 = 0.056079865
        else:
            var92 = 0.230336
    if input[0] < 3.0:
        if input[0] < 2.0:
            var93 = 0.004346466
        else:
            var93 = -0.022372438
    else:
        if input[0] < 5.0:
            var93 = 0.053276062
        else:
            var93 = 0.21881866
    if input[0] < 5.0:
        var94 = 0.05061188
    else:
        var94 = 0.20787811
    if input[1] < 180.0:
        if input[1] < 50.0:
            var95 = -0.023784637
        else:
            var95 = 0.0015983582
    else:
        if input[1] < 500.0:
            var95 = 0.048081208
        else:
            var95 = 0.19748382
    if input[0] < 3.0:
        if input[0] < 2.0:
            var96 = 0.0015182495
        else:
            var96 = -0.022595216
    else:
        if input[0] < 5.0:
            var96 = 0.045677185
        else:
            var96 = 0.18760987
    if input[1] < 180.0:
        if input[1] < 50.0:
            var97 = -0.021465302
        else:
            var97 = 0.0014423371
    else:
        if input[1] < 500.0:
            var97 = 0.043392945
        else:
            var97 = 0.17822877
    if input[0] < 3.0:
        if input[0] < 2.0:
            var98 = 0.0013702393
        else:
            var98 = -0.020391846
    else:
        if input[0] < 5.0:
            var98 = 0.041223146
        else:
            var98 = 0.16931763
    if input[0] < 3.0:
        if input[0] < 2.0:
            var99 = 0.0013015748
        else:
            var99 = -0.019372178
    else:
        if input[0] < 5.0:
            var99 = 0.039161682
        else:
            var99 = 0.16085206
    if input[0] < 5.0:
        if input[0] < 2.0:
            var100 = 0.0012363434
        else:
            var100 = 0.03720398
    else:
        var100 = 0.15280914
    if input[0] < 3.0:
        if input[0] < 2.0:
            var101 = 0.0011745453
        else:
            var101 = -0.020263672
    else:
        if input[0] < 5.0:
            var101 = 0.035343934
        else:
            var101 = 0.14516906
    if input[0] < 3.0:
        if input[0] < 2.0:
            var102 = 0.001115799
        else:
            var102 = -0.019250488
    else:
        if input[0] < 5.0:
            var102 = 0.033576965
        else:
            var102 = 0.13791047
    if input[0] < 3.0:
        if input[0] < 2.0:
            var103 = 0.0010601043
        else:
            var103 = -0.01828804
    else:
        if input[0] < 5.0:
            var103 = 0.0318985
        else:
            var103 = 0.13101502
    if input[0] < 3.0:
        if input[0] < 2.0:
            var104 = 0.0010070801
        else:
            var104 = -0.017373657
    else:
        if input[0] < 5.0:
            var104 = 0.030303955
        else:
            var104 = 0.124464415
    if input[0] < 3.0:
        if input[0] < 2.0:
            var105 = 0.0009567261
        else:
            var105 = -0.016505051
    else:
        if input[0] < 5.0:
            var105 = 0.028788758
        else:
            var105 = 0.118241884
    if input[0] < 5.0:
        if input[0] < 2.0:
            var106 = 0.00090904237
        else:
            var106 = 0.02734909
    else:
        var106 = 0.1123291
    if input[0] < 3.0:
        if input[0] < 2.0:
            var107 = 0.0008636475
        else:
            var107 = -0.0170475
    else:
        if input[0] < 5.0:
            var107 = 0.025981903
        else:
            var107 = 0.10671234
    if input[0] < 3.0:
        if input[0] < 2.0:
            var108 = 0.0008205414
        else:
            var108 = -0.016195297
    else:
        if input[0] < 5.0:
            var108 = 0.024682617
        else:
            var108 = 0.10137635
    if input[0] < 5.0:
        var109 = 0.023448182
    else:
        var109 = 0.096307375
    if input[0] < 3.0:
        var110 = -0.016557693
    else:
        if input[0] < 5.0:
            var110 = 0.022275543
        else:
            var110 = 0.0914917
    if input[0] < 3.0:
        if input[0] < 2.0:
            var111 = 0.0004348755
        else:
            var111 = -0.015729904
    else:
        if input[0] < 5.0:
            var111 = 0.021161651
        else:
            var111 = 0.08691712
    if input[0] < 3.0:
        var112 = -0.014943314
    else:
        if input[0] < 5.0:
            var112 = 0.020103455
        else:
            var112 = 0.08257141
    if input[1] < 180.0:
        if input[1] < 50.0:
            var113 = -0.014196015
        else:
            var113 = 0.001160431
    else:
        if input[1] < 500.0:
            var113 = 0.0190979
        else:
            var113 = 0.07844239
    if input[0] < 3.0:
        if input[0] < 2.0:
            var114 = 0.0011024475
        else:
            var114 = -0.013486099
    else:
        if input[0] < 5.0:
            var114 = 0.0181427
        else:
            var114 = 0.07452088
    if input[1] < 180.0:
        if input[1] < 50.0:
            var115 = -0.012811661
        else:
            var115 = 0.0010475159
    else:
        if input[1] < 500.0:
            var115 = 0.017235566
        else:
            var115 = 0.07079468
    if input[0] < 3.0:
        if input[0] < 2.0:
            var116 = 0.0009952545
        else:
            var116 = -0.0121711735
    else:
        if input[0] < 5.0:
            var116 = 0.016373444
        else:
            var116 = 0.06725464
    if input[0] < 3.0:
        var117 = -0.011562729
    else:
        if input[0] < 5.0:
            var117 = 0.01555481
        else:
            var117 = 0.063891605
    if input[0] < 3.0:
        var118 = -0.010984421
    else:
        if input[0] < 5.0:
            var118 = 0.014777374
        else:
            var118 = 0.060696412
    if input[1] < 180.0:
        if input[1] < 50.0:
            var119 = -0.010435104
        else:
            var119 = 0.002073288
    else:
        if input[1] < 500.0:
            var119 = 0.014038849
        else:
            var119 = 0.05766144
    if input[0] < 5.0:
        if input[0] < 2.0:
            var120 = 0.0019695282
        else:
            var120 = 0.013336944
    else:
        var120 = 0.054779053
    if input[0] < 3.0:
        if input[0] < 2.0:
            var121 = 0.001871109
        else:
            var121 = -0.010580063
    else:
        if input[0] < 5.0:
            var121 = 0.012670136
        else:
            var121 = 0.0520401
    if input[0] < 3.0:
        if input[0] < 2.0:
            var122 = 0.0017776489
        else:
            var122 = -0.010050965
    else:
        if input[0] < 5.0:
            var122 = 0.012036896
        else:
            var122 = 0.049438477
    if input[0] < 3.0:
        var123 = -0.009548569
    else:
        if input[0] < 5.0:
            var123 = 0.011434937
        else:
            var123 = 0.046966553
    if input[1] < 180.0:
        if input[1] < 50.0:
            var124 = -0.009070969
        else:
            var124 = 0.0021663667
    else:
        if input[1] < 500.0:
            var124 = 0.010863495
        else:
            var124 = 0.044618227
    if input[0] < 3.0:
        if input[0] < 2.0:
            var125 = 0.0020580292
        else:
            var125 = -0.008617401
    else:
        if input[0] < 5.0:
            var125 = 0.010320283
        else:
            var125 = 0.042387392
    if input[0] < 5.0:
        if input[0] < 2.0:
            var126 = 0.0019550323
        else:
            var126 = 0.009804535
    else:
        var126 = 0.040267944
    if input[0] < 3.0:
        if input[0] < 2.0:
            var127 = 0.0018573761
        else:
            var127 = -0.008676529
    else:
        if input[0] < 5.0:
            var127 = 0.009313965
        else:
            var127 = 0.038253784
    if input[1] < 500.0:
        var128 = 0.008848572
    else:
        var128 = 0.036340334
    if input[0] < 3.0:
        if input[0] < 2.0:
            var129 = 0.0013221741
        else:
            var129 = -0.008685303
    else:
        if input[0] < 5.0:
            var129 = 0.008406067
        else:
            var129 = 0.03452301
    if input[0] < 3.0:
        if input[0] < 2.0:
            var130 = 0.0012561799
        else:
            var130 = -0.00825119
    else:
        if input[0] < 5.0:
            var130 = 0.007985688
        else:
            var130 = 0.032797243
    if input[0] < 3.0:
        if input[0] < 2.0:
            var131 = 0.0011932374
        else:
            var131 = -0.00783844
    else:
        if input[0] < 5.0:
            var131 = 0.00758667
        else:
            var131 = 0.031156922
    if input[0] < 3.0:
        if input[0] < 2.0:
            var132 = 0.0011337281
        else:
            var132 = -0.0074466704
    else:
        if input[0] < 5.0:
            var132 = 0.007207489
        else:
            var132 = 0.029599
    if input[0] < 3.0:
        if input[0] < 2.0:
            var133 = 0.0010768891
        else:
            var133 = -0.007074356
    else:
        if input[0] < 5.0:
            var133 = 0.0068473816
        else:
            var133 = 0.028118897
    if input[0] < 3.0:
        var134 = -0.006720734
    else:
        if input[0] < 5.0:
            var134 = 0.006504822
        else:
            var134 = 0.026713563
    if input[0] < 3.0:
        if input[0] < 2.0:
            var135 = 0.0013591767
        else:
            var135 = -0.006384659
    else:
        if input[0] < 5.0:
            var135 = 0.0061798096
        else:
            var135 = 0.02537842
    if input[0] < 3.0:
        if input[0] < 2.0:
            var136 = 0.001291275
        else:
            var136 = -0.0060653687
    else:
        if input[0] < 5.0:
            var136 = 0.005870819
        else:
            var136 = 0.024108887
    var137 = var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100 + var101 + var102 + var103 + var104 + var105 + var106 + var107 + var108 + var109 + var110 + var111 + var112 + var113 + var114 + var115 + var116 + var117 + var118 + var119 + var120 + var121 + var122 + var123 + var124 + var125 + var126 + var127 + var128 + var129 + var130 + var131 + var132 + var133 + var134 + var135 + var136
    if input[1] < 50.0:
        var138 = -0.0057621
    else:
        if input[1] < 500.0:
            var138 = 0.0055770874
        else:
            var138 = 0.022903442
    if input[0] < 5.0:
        if input[0] < 2.0:
            var139 = 0.00094795227
        else:
            var139 = 0.0052978517
    else:
        var139 = 0.021759033
    if input[0] < 3.0:
        if input[0] < 2.0:
            var140 = 0.00090065005
        else:
            var140 = -0.0057388307
    else:
        if input[0] < 5.0:
            var140 = 0.0050331117
        else:
            var140 = 0.020671083
    if input[0] < 3.0:
        if input[0] < 2.0:
            var141 = 0.0008556366
        else:
            var141 = -0.0054519656
    else:
        if input[0] < 5.0:
            var141 = 0.0047813416
        else:
            var141 = 0.019638062
    if input[0] < 3.0:
        if input[0] < 2.0:
            var142 = 0.000812912
        else:
            var142 = -0.0051792148
    else:
        if input[0] < 5.0:
            var142 = 0.0045425417
        else:
            var142 = 0.018655395
    if input[1] < 50.0:
        var143 = -0.0049201967
    else:
        if input[1] < 500.0:
            var143 = 0.004315186
        else:
            var143 = 0.017723083
    if input[1] < 180.0:
        if input[1] < 50.0:
            var144 = -0.0046741487
        else:
            var144 = 0.0005561829
    else:
        if input[1] < 500.0:
            var144 = 0.0040992736
        else:
            var144 = 0.016836548
    if input[0] < 3.0:
        var145 = -0.0044403076
    else:
        if input[0] < 5.0:
            var145 = 0.003894043
        else:
            var145 = 0.015994264
    if input[0] < 5.0:
        if input[0] < 2.0:
            var146 = 0.00075035094
        else:
            var146 = 0.0036994934
    else:
        var146 = 0.015194702
    if input[0] < 3.0:
        if input[0] < 2.0:
            var147 = 0.00071296695
        else:
            var147 = -0.0044033052
    else:
        if input[0] < 5.0:
            var147 = 0.0035148622
        else:
            var147 = 0.014434814
    if input[0] < 3.0:
        if input[0] < 2.0:
            var148 = 0.00067749026
        else:
            var148 = -0.004183197
    else:
        if input[0] < 5.0:
            var148 = 0.003339386
        else:
            var148 = 0.013713074
    if input[0] < 3.0:
        if input[0] < 2.0:
            var149 = 0.0006435394
        else:
            var149 = -0.003974152
    else:
        if input[0] < 5.0:
            var149 = 0.0031723024
        else:
            var149 = 0.013027954
    if input[0] < 3.0:
        if input[0] < 2.0:
            var150 = 0.000611496
        else:
            var150 = -0.003775406
    else:
        if input[0] < 5.0:
            var150 = 0.0030136108
        else:
            var150 = 0.012376404
    if input[1] < 500.0:
        if input[1] < 180.0:
            var151 = 0.0005809784
        else:
            var151 = 0.002862549
    else:
        var151 = 0.011756897
    if input[0] < 3.0:
        if input[0] < 2.0:
            var152 = 0.0005519867
        else:
            var152 = -0.00361557
    else:
        if input[0] < 5.0:
            var152 = 0.0027191162
        else:
            var152 = 0.011169434
    if input[0] < 3.0:
        var153 = -0.0034347535
    else:
        if input[0] < 5.0:
            var153 = 0.002583313
        else:
            var153 = 0.010610962
    if input[0] < 3.0:
        if input[0] < 2.0:
            var154 = 0.00069618225
        else:
            var154 = -0.0032630921
    else:
        if input[0] < 5.0:
            var154 = 0.0024543763
        else:
            var154 = 0.010079957
    if input[0] < 3.0:
        if input[0] < 2.0:
            var155 = 0.00066146854
        else:
            var155 = -0.0030998231
    else:
        if input[0] < 5.0:
            var155 = 0.002331543
        else:
            var155 = 0.009576417
    if input[0] < 3.0:
        if input[0] < 2.0:
            var156 = 0.0006282806
        else:
            var156 = -0.0029449463
    else:
        if input[0] < 5.0:
            var156 = 0.0022148134
        else:
            var156 = 0.00909729
    if input[0] < 3.0:
        var157 = -0.002797699
    else:
        if input[0] < 5.0:
            var157 = 0.0021041872
        else:
            var157 = 0.0086425785
    if input[0] < 3.0:
        if input[0] < 2.0:
            var158 = 0.0007369995
        else:
            var158 = -0.0026576996
    else:
        if input[0] < 5.0:
            var158 = 0.0019989014
        else:
            var158 = 0.008210755
    if input[0] < 3.0:
        if input[0] < 2.0:
            var159 = 0.00069999695
        else:
            var159 = -0.0025249482
    else:
        if input[0] < 5.0:
            var159 = 0.0018989564
        else:
            var159 = 0.007800293
    if input[0] < 3.0:
        if input[0] < 2.0:
            var160 = 0.00066490175
        else:
            var160 = -0.0023986816
    else:
        if input[0] < 5.0:
            var160 = 0.0018043518
        else:
            var160 = 0.007409668
    if input[1] < 180.0:
        if input[1] < 50.0:
            var161 = -0.0022789002
        else:
            var161 = 0.0006317139
    else:
        if input[1] < 500.0:
            var161 = 0.0017143249
        else:
            var161 = 0.0070388797
    if input[0] < 5.0:
        var162 = 0.0014859517
    else:
        var162 = 0.0066864016
    if input[0] < 3.0:
        if input[0] < 2.0:
            var163 = 0.0005256653
        else:
            var163 = -0.0022392273
    else:
        if input[0] < 5.0:
            var163 = 0.0015548706
        else:
            var163 = 0.006352234
    if input[0] < 3.0:
        var164 = -0.0021270753
    else:
        if input[0] < 5.0:
            var164 = 0.0014770508
        else:
            var164 = 0.006034851
    if input[0] < 3.0:
        if input[0] < 2.0:
            var165 = 0.00060577394
        else:
            var165 = -0.0020206452
    else:
        if input[0] < 5.0:
            var165 = 0.0014030457
        else:
            var165 = 0.0057327272
    if input[0] < 3.0:
        if input[0] < 2.0:
            var166 = 0.00057563785
        else:
            var166 = -0.0019195557
    else:
        if input[0] < 5.0:
            var166 = 0.0013328552
        else:
            var166 = 0.0054458617
    if input[0] < 3.0:
        var167 = -0.0018234253
    else:
        if input[0] < 5.0:
            var167 = 0.0012664795
        else:
            var167 = 0.0051742555
    if input[1] < 500.0:
        var168 = 0.0012275696
    else:
        var168 = 0.004914856
    if input[0] < 5.0:
        var169 = 0.001145935
    else:
        var169 = 0.0046691895
    if input[0] < 5.0:
        var170 = 0.0010696411
    else:
        var170 = 0.00443573
    if input[1] < 50.0:
        var171 = -0.0019042969
    else:
        if input[1] < 500.0:
            var171 = 0.0009984334
        else:
            var171 = 0.0042144777
    if input[0] < 3.0:
        var172 = -0.0018089295
    else:
        if input[0] < 5.0:
            var172 = 0.000981903
        else:
            var172 = 0.004003906
    if input[1] < 50.0:
        var173 = -0.0017185211
    else:
        if input[0] < 5.0:
            var173 = 0.00095977786
        else:
            var173 = 0.0038040162
    if input[1] < 50.0:
        var174 = -0.0016326904
    else:
        if input[1] < 500.0:
            var174 = 0.00088500977
        else:
            var174 = 0.0036132813
    if input[1] < 50.0:
        var175 = -0.0015510559
    else:
        if input[0] < 5.0:
            var175 = 0.00083669025
        else:
            var175 = 0.0034332275
    if input[1] < 50.0:
        var176 = -0.0014736176
    else:
        if input[0] < 5.0:
            var176 = 0.0007807414
        else:
            var176 = 0.0032623291
    if input[1] < 50.0:
        var177 = -0.0013999939
    else:
        if input[0] < 5.0:
            var177 = 0.0007288615
        else:
            var177 = 0.0030990602
    if input[0] < 3.0:
        if input[0] < 2.0:
            var178 = 0.00029678346
        else:
            var178 = -0.0013298035
    else:
        if input[0] < 5.0:
            var178 = 0.0007232666
        else:
            var178 = 0.0029434205
    if input[1] < 180.0:
        if input[1] < 50.0:
            var179 = -0.0012634278
        else:
            var179 = 0.00028190613
    else:
        if input[1] < 500.0:
            var179 = 0.00068740844
        else:
            var179 = 0.002796936
    if input[0] < 3.0:
        var180 = -0.0012001038
    else:
        if input[0] < 5.0:
            var180 = 0.00065307616
        else:
            var180 = 0.0026565553
    if input[0] < 5.0:
        var181 = 0.0006319682
    else:
        var181 = 0.0025238039
    if input[1] < 500.0:
        var182 = 0.00059000653
    else:
        var182 = 0.0023971559
    if input[1] < 50.0:
        var183 = -0.0012012481
    else:
        if input[0] < 5.0:
            var183 = 0.000550588
        else:
            var183 = 0.0022766113
    if input[2] < 150.75:
        var184 = -0.0011413575
    else:
        if input[2] < 300.0:
            var184 = 0.00053176883
        else:
            var184 = 0.0021621704
    if input[1] < 50.0:
        var185 = -0.001084137
    else:
        if input[1] < 500.0:
            var185 = 0.0005343119
        else:
            var185 = 0.002053833
    if input[0] < 5.0:
        var186 = 0.00047836304
    else:
        var186 = 0.0019515991
    if input[3] < 50.0:
        var187 = -0.0010540009
    else:
        if input[0] < 5.0:
            var187 = 0.00046691895
        else:
            var187 = 0.0018539429
    if input[0] < 5.0:
        var188 = 0.0004310608
    else:
        var188 = 0.0017608643
    if input[1] < 50.0:
        var189 = -0.0010231019
    else:
        if input[1] < 500.0:
            var189 = 0.00040690103
        else:
            var189 = 0.0016723633
    if input[3] < 50.0:
        var190 = -0.0009719849
    else:
        if input[0] < 5.0:
            var190 = 0.00037968953
        else:
            var190 = 0.0015884399
    if input[0] < 5.0:
        var191 = 0.00035425823
    else:
        var191 = 0.0015090943
    if input[0] < 5.0:
        var192 = 0.0003308614
    else:
        var192 = 0.0014343262
    var193 = var137 + var138 + var139 + var140 + var141 + var142 + var143 + var144 + var145 + var146 + var147 + var148 + var149 + var150 + var151 + var152 + var153 + var154 + var155 + var156 + var157 + var158 + var159 + var160 + var161 + var162 + var163 + var164 + var165 + var166 + var167 + var168 + var169 + var170 + var171 + var172 + var173 + var174 + var175 + var176 + var177 + var178 + var179 + var180 + var181 + var182 + var183 + var184 + var185 + var186 + var187 + var188 + var189 + var190 + var191 + var192
    if input[1] < 50.0:
        var194 = -0.000957489
    else:
        if input[0] < 5.0:
            var194 = 0.00030873617
        else:
            var194 = 0.0013626099
    if input[1] < 50.0:
        var195 = -0.00090942386
    else:
        if input[1] < 500.0:
            var195 = 0.0002883911
        else:
            var195 = 0.0012939454
    if input[5] < 1.0:
        var196 = -0.00086402893
    else:
        if input[0] < 5.0:
            var196 = 0.0002690633
        else:
            var196 = 0.0012298584
    if input[1] < 50.0:
        var197 = -0.00082092284
    else:
        if input[0] < 5.0:
            var197 = 0.0002510071
        else:
            var197 = 0.0011688232
    if input[3] < 50.0:
        var198 = -0.00077972416
    else:
        if input[0] < 5.0:
            var198 = 0.00023447674
        else:
            var198 = 0.0011108399
    if input[3] < 50.0:
        var199 = -0.0007408142
    else:
        if input[0] < 5.0:
            var199 = 0.00021896363
        else:
            var199 = 0.0010559083
    if input[1] < 50.0:
        var200 = -0.00070381165
    else:
        if input[0] < 5.0:
            if input[0] < 2.0:
                var200 = 0.000048828126
            else:
                var200 = 0.00025787353
        else:
            var200 = 0.0010025025
    if input[1] < 50.0:
        var201 = -0.00066871644
    else:
        if input[0] < 5.0:
            if input[0] < 2.0:
                var201 = 0.000046539306
            else:
                var201 = 0.00024490358
        else:
            var201 = 0.00095214846
    if input[1] < 50.0:
        var202 = -0.0006351471
    else:
        if input[1] < 500.0:
            var202 = 0.00023269653
        else:
            var202 = 0.0009048462
    if input[0] < 3.0:
        if input[0] < 2.0:
            var203 = 0.000032806398
        else:
            var203 = -0.0006034851
    else:
        if input[0] < 5.0:
            var203 = 0.00022125244
        else:
            var203 = 0.0008590698
    if input[0] < 3.0:
        if input[0] < 2.0:
            var204 = 0.000031280517
        else:
            var204 = -0.000573349
    else:
        if input[0] < 5.0:
            var204 = 0.00021057129
        else:
            var204 = 0.0008163452
    if input[0] < 5.0:
        var205 = 0.00019989014
    else:
        var205 = 0.0007751465
    if input[1] < 50.0:
        var206 = -0.000554657
    else:
        if input[1] < 500.0:
            var206 = 0.00018997192
        else:
            var206 = 0.0007369995
    if input[0] < 3.0:
        var207 = -0.0005268097
    else:
        if input[0] < 5.0:
            var207 = 0.00018081666
        else:
            var207 = 0.00070037844
    if input[1] < 50.0:
        var208 = -0.00050048827
    else:
        if input[1] < 500.0:
            var208 = 0.00013885499
        else:
            var208 = 0.00066528324
    if input[1] < 500.0:
        var209 = 0.0001296997
    else:
        var209 = 0.0006317139
    if input[1] < 50.0:
        var210 = -0.00048179628
    else:
        if input[1] < 180.0:
            var210 = 0.000023269653
        else:
            var210 = 0.0005055746
    if input[0] < 5.0:
        var211 = 0.00010375977
    else:
        var211 = 0.0005737305
    if input[1] < 50.0:
        var212 = -0.00046310425
    else:
        if input[0] < 5.0:
            var212 = 0.000096639
        else:
            var212 = 0.0005447388
    if input[1] < 50.0:
        var213 = -0.0004398346
    else:
        if input[0] < 5.0:
            var213 = 0.00009028117
        else:
            var213 = 0.000517273
    if input[1] < 50.0:
        var214 = -0.00041770935
    else:
        if input[0] < 5.0:
            var214 = 0.00008417766
        else:
            var214 = 0.000491333
    if input[0] < 3.0:
        if input[0] < 2.0:
            var215 = 0.0000030517579
        else:
            var215 = -0.00039672852
    else:
        if input[0] < 5.0:
            var215 = 0.00011444092
        else:
            var215 = 0.00046691895
    if input[0] < 5.0:
        var216 = 0.00007425944
    else:
        var216 = 0.00044403077
    if input[1] < 50.0:
        var217 = -0.0003807068
    else:
        if input[0] < 5.0:
            var217 = 0.00006917318
        else:
            var217 = 0.00042114258
    if input[0] < 3.0:
        var218 = -0.0003616333
    else:
        var218 = 0.00033365886
    if input[0] < 3.0:
        var219 = -0.00034370422
    else:
        if input[0] < 5.0:
            var219 = 0.00008392334
        else:
            var219 = 0.0003829956
    if input[1] < 50.0:
        var220 = -0.00032653808
    else:
        if input[0] < 5.0:
            var220 = 0.00007349651
        else:
            var220 = 0.0003631592
    if input[1] < 50.0:
        var221 = -0.0003101349
    else:
        if input[0] < 5.0:
            var221 = 0.000068410234
        else:
            var221 = 0.00034484864
    if input[0] < 3.0:
        var222 = -0.00029449465
    else:
        if input[0] < 5.0:
            var222 = 0.00007247925
        else:
            var222 = 0.00032806396
    if input[1] < 50.0:
        var223 = -0.00027961732
    else:
        if input[1] < 500.0:
            var223 = 0.000071462
        else:
            var223 = 0.0003112793
    if input[0] < 5.0:
        var224 = 0.00006484985
    else:
        var224 = 0.0002960205
    if input[1] < 50.0:
        var225 = -0.0002685547
    else:
        if input[0] < 5.0:
            var225 = 0.000062561034
        else:
            var225 = 0.0002807617
    if input[1] < 50.0:
        var226 = -0.00025520325
    else:
        if input[0] < 5.0:
            var226 = 0.000058492024
        else:
            var226 = 0.0002670288
    if input[1] < 50.0:
        var227 = -0.00024261475
    else:
        if input[0] < 5.0:
            var227 = 0.000054423017
        else:
            var227 = 0.0002532959
    if input[1] < 50.0:
        var228 = -0.00023040772
    else:
        if input[0] < 5.0:
            var228 = 0.00005060832
        else:
            var228 = 0.00024108887
    if input[3] < 50.0:
        var229 = -0.00021896363
    else:
        if input[0] < 5.0:
            var229 = 0.00004730225
        else:
            var229 = 0.00022888184
    if input[1] < 50.0:
        var230 = -0.000207901
    else:
        if input[1] < 500.0:
            var230 = 0.00004425049
        else:
            var230 = 0.0002166748
    if input[3] < 50.0:
        var231 = -0.00019760132
    else:
        if input[0] < 5.0:
            var231 = 0.00004119873
        else:
            var231 = 0.00020599365
    if input[1] < 50.0:
        var232 = -0.00018768311
    else:
        if input[0] < 5.0:
            var232 = 0.000038401286
        else:
            var232 = 0.0001953125
    if input[1] < 50.0:
        var233 = -0.00017814637
    else:
        if input[1] < 500.0:
            var233 = 0.000035603844
        else:
            var233 = 0.00018615722
    if input[0] < 5.0:
        var234 = 0.000033315024
    else:
        var234 = 0.00017700196
    if input[1] < 50.0:
        var235 = -0.00017089843
    else:
        if input[0] < 5.0:
            var235 = 0.000031280517
        else:
            var235 = 0.00016784668
    if input[1] < 50.0:
        var236 = -0.00016899109
    else:
        if input[0] < 5.0:
            var236 = 0.000020345053
        else:
            var236 = 0.00015258789
    if input[0] < 3.0:
        var237 = -0.00016059876
    else:
        var237 = 0.000115966795
    if input[5] < 1.0:
        var238 = -0.00015258789
    else:
        if input[0] < 5.0:
            var238 = 0.000020345053
        else:
            var238 = 0.00013885499
    if input[3] < 50.0:
        var239 = -0.0001449585
    else:
        var239 = 0.00007991791
    if input[3] < 50.0:
        var240 = -0.00013771058
    else:
        if input[0] < 5.0:
            var240 = 0.000013987224
        else:
            var240 = 0.00012664795
    if input[1] < 50.0:
        var241 = -0.00013084411
    else:
        var241 = 0.000069999696
    if input[1] < 50.0:
        var242 = -0.00012435914
    else:
        if input[0] < 5.0:
            var242 = 0.000008138021
        else:
            var242 = 0.00011749268
    if input[1] < 50.0:
        var243 = -0.000118255615
    else:
        var243 = 0.00008290609
    if input[1] < 50.0:
        var244 = -0.0001121521
    else:
        if input[0] < 5.0:
            var244 = 0.0000020345053
        else:
            var244 = 0.00010681152
    if input[2] < 150.75:
        var245 = -0.000078582765
    else:
        var245 = 0.00006968181
    if input[3] < 50.0:
        var246 = -0.000105285646
    else:
        var246 = 0.000046348574
    var247 = var193 + var194 + var195 + var196 + var197 + var198 + var199 + var200 + var201 + var202 + var203 + var204 + var205 + var206 + var207 + var208 + var209 + var210 + var211 + var212 + var213 + var214 + var215 + var216 + var217 + var218 + var219 + var220 + var221 + var222 + var223 + var224 + var225 + var226 + var227 + var228 + var229 + var230 + var231 + var232 + var233 + var234 + var235 + 0.00013020834 + var236 + var237 + var238 + var239 + var240 + var241 + var242 + var243 + var244 + 0.000051879884 + var245 + var246
    if input[0] < 5.0:
        var248 = -0.0000073750816
    else:
        var248 = 0.00009002686
    if input[1] < 50.0:
        var249 = -0.00010185242
    else:
        var249 = 0.000055948894
    if input[0] < 5.0:
        var250 = -0.000060462953
    else:
        var250 = 0.00007934571
    if input[0] < 5.0:
        var251 = -0.000055885317
    else:
        var251 = 0.00007476807
    if input[1] < 50.0:
        var252 = -0.000093841554
    else:
        var252 = 0.000031089785
    if input[0] < 5.0:
        var253 = -0.00005092621
    else:
        var253 = 0.00007019043
    if input[0] < 3.0:
        var254 = -0.00008659363
    else:
        var254 = 0.000044759116
    if input[1] < 50.0:
        var255 = -0.00008239746
    else:
        var255 = 0.000029945373
    if input[0] < 5.0:
        var256 = -0.00004348755
    else:
        var256 = 0.00006408692
    if input[1] < 50.0:
        var257 = -0.000075912474
    else:
        var257 = 0.000028419496
    if input[1] < 500.0:
        var258 = -0.000039672854
    else:
        var258 = 0.00005950928
    if input[1] < 50.0:
        var259 = -0.00007019043
    else:
        var259 = 0.00002670288
    if input[1] < 500.0:
        var260 = -0.000047810874
    else:
        var260 = 0.00005340576
    if input[1] < 50.0:
        var261 = -0.000065612796
    else:
        var261 = 0.00002307892
    if input[0] < 3.0:
        var262 = -0.00006217957
    else:
        var262 = 0.000030517578
    return var247 + 0.000042533877 + var248 + var249 + 0.000051879884 + var250 + var251 + var252 + var253 + var254 + var255 + var256 + var257 + var258 + var259 + 0.000024414063 + var260 + var261 + var262 + 0.000028483073 + -0.000009307862 + -0.00000869751 + -0.000008087159 + 0.00002040863 + -0.000009307862 + -0.00000869751 + -0.000008087159 + -0.0000087738035 + -0.0000082015995 + -0.0000062561035 + -0.000005950928 + -0.0000072479247 + -0.000005340576 + -0.0000050354006 + -0.0000047302246 + 0.00002269745 + 0.000020980835 + -0.000008087159 + -0.000007476807 + -0.000007171631 + -0.0000068664554 + -0.00000656128 + -0.0000062561035 + -0.000005950928 + -0.000005645752 + -0.000005340576 + -0.0000050354006 + -0.0000047302246 + -0.000004425049 + 0.00002193451 + -0.000005950928 + -0.0000087738035 + -0.0000050354006 + -0.0000047302246 + -0.000007820129 + 0.000025939942
