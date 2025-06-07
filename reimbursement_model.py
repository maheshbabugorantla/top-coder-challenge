def score(input):
    if input[1] <= 700.0:
        if input[1] <= 150.0:
            if input[2] <= 50.25:
                var0 = 13.0
            else:
                if input[1] <= 75.0:
                    var0 = 30.05
                else:
                    var0 = 44.06
        else:
            if input[2] <= 350.25:
                if input[2] <= 188.0250015258789:
                    if input[2] <= 135.82500076293945:
                        var0 = 84.59
                    else:
                        var0 = 75.075
                else:
                    if input[4] <= 15.0:
                        var0 = 95.0
                    else:
                        var0 = 110.03
            else:
                var0 = 150.05
    else:
        if input[4] <= 45.0:
            if input[2] <= 650.1000061035156:
                if input[3] <= 83.33333206176758:
                    var0 = 215.0
                else:
                    var0 = 200.0
            else:
                var0 = 300.02
        else:
            var0 = 445.07
    return var0
