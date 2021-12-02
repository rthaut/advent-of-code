import re

passwords = [
"2-4 r: prrmspx",
"5-6 p: hpzplphxb",
"5-8 t: ttttbtttttc",
"1-6 k: kkkkkk",
"1-3 q: qqqq",
"4-8 t: pctpfqtrtttmvptvfmws",
"3-5 z: zznzslv",
"12-14 h: hhhhhhhhhhhhhhhh",
"14-15 v: vvvvvvvvhvvvvdmvv",
"8-17 x: xxxxxxdxxxxxxxckxx",
"11-12 f: gkfjnffjfcmfwk",
"10-12 s: xsgsssshbmsbnss",
"6-15 s: sssssnsssssssss",
"2-8 d: qnqtrqdrnvq",
"5-7 k: lhxkkkk",
"4-5 k: xkkkk",
"10-16 v: vvvvvvvvvcvvvvvpvv",
"1-6 f: ffffflfffffff",
"4-5 x: fxdnq",
"10-12 p: mkspmhlldqjh",
"10-12 r: rcvzzcbdgrcr",
"4-7 r: rxbkrrrzrrrtrrr",
"18-19 k: kkkkkkkkkkkkkkkkkkk",
"1-2 f: sfffffffffffffffff",
"1-5 z: mhkzwdxklf",
"2-3 r: qzbgrghkmlpxdvd",
"2-3 q: mqqpcxbqdf",
"7-8 r: rrrrfrrj",
"1-9 x: vmxsmwhnxccf",
"9-10 t: ttttttttppt",
"2-4 x: rxxqxx",
"16-17 k: jkfmnwkkztnxvlkkw",
"3-4 c: ccbpccccczpcccc",
"5-8 g: ggggjggg",
"1-3 z: szzzzz",
"8-9 l: xnllznclz",
"4-10 m: pkmmptjvgsnwmxm",
"1-2 r: mbrrtkrjdr",
"1-3 c: ccqscsxcnctwlvm",
"4-6 p: ppppppppp",
"3-5 d: wdddxvmnbdhvzdgqbdm",
"5-7 n: nnwbsnqnnvn",
"2-11 j: sgbxjvqnbmq",
"5-13 q: qqqkpqqqsqqqxqqqq",
"2-12 m: kvwlwmmvhbpgmnzfddms",
"2-4 j: kjgcpgxgcphkqjjmbwd",
"3-6 v: tdvlvv",
"10-20 n: tnmhnlznnpnmnfnngnnn",
"4-7 h: hhhhhhhh",
"9-11 m: mmmmmmmmrmm",
"7-9 b: mbnbbbbqk",
"9-10 z: fqzzzmzzzzj",
"3-15 s: chdpzcpgsgrkhss",
"3-4 k: kklz",
"1-5 q: ltqqqxcndqrq",
"9-17 m: mmmmmmmmqdlmmxbmtmmm",
"14-16 k: kkkkkkmkkkkkjtkkk",
"8-9 k: kkkkkqkkxlk",
"2-6 n: kbhhjhdmgtn",
"3-8 w: rcwwwkqwbwkwmdqtwmw",
"10-11 x: snkbxmwqwxp",
"2-5 m: pmhmp",
"6-7 b: bbbbbbq",
"3-7 l: cfqmljq",
"9-13 q: qzqqqqqqqlqdt",
"2-10 w: kmwqwtwkssd",
"4-13 t: ttblttttttttftt",
"14-17 l: llllllwllllllwllclll",
"3-4 p: xzps",
"10-14 b: bjbbbbbpbdbbbb",
"5-7 v: jlvhjtvx",
"6-9 r: bscrrrrcrphffdw",
"5-7 r: brrvjrxfrljwxp",
"15-16 b: bbbbbbbbbbbbbbbb",
"7-8 h: bchfxxshh",
"2-13 z: zzqzzzzzzzzzzzz",
"1-5 b: bbbbrbbhbbbbbcb",
"2-3 k: zkkzjld",
"4-6 f: fnffffff",
"8-11 d: qdvdddddndphdndmgdkp",
"17-18 q: qqqkqqqqqqcqqqqtqq",
"11-16 m: mmmwmwxvmmmmmmmmmmm",
"12-13 v: vvvvfxvgblvvk",
"4-6 v: vsvvvvv",
"2-4 p: rqgm",
"7-8 r: rrrrrfrf",
"2-4 j: xpjjl",
"7-8 b: wdpbvwbb",
"15-16 k: fkkkskkkmkkkkkkk",
"10-14 s: shkscsqjszstssv",
"3-4 l: lllw",
"2-4 n: gjbnlsxvqmvxgcwntvvs",
"6-12 l: lclllgllllllll",
"16-17 b: bbbbbbbbbbbbbbbbbbb",
"7-8 q: pqqqqqwq",
"1-2 r: rrzsr",
"1-3 r: rrfr",
"16-17 f: fffcfffffjfmrzqffnr",
"15-17 h: bhzhhfndwgdhlhhhjh",
"7-11 t: vtwnrwzczmtwn",
"3-6 v: vvvvvmvvvvvv",
"4-5 s: ssptsss",
"1-3 t: ttntq",
"5-9 g: ggggtgggcg",
"7-8 h: hcjdkphhb",
"15-17 j: jjjjjmjjjjtjgvnxk",
"3-4 q: qqqq",
"5-7 g: lggsjqlg",
"11-18 m: mmmmmmmmmmqmmmmmmf",
"1-14 x: xxxxcxxxxxxxxxxxxx",
"7-8 f: ffffffbffff",
"3-4 t: xmct",
"3-4 x: xxtcd",
"1-11 x: xcnxxxxvxlxkmcrxn",
"8-11 h: hgnhkhhshhnhhzdhllw",
"8-10 z: zdzzzzzrpvvzzqz",
"6-7 r: lrbrrprrxr",
"6-10 n: fnnwnpnnjnhmnntqn",
"10-15 b: bbbbbbbbbwbbbbbbbbbb",
"13-16 z: zzzzzzzwzzzzvvzkztjz",
"5-6 t: xntkwthxbdtlmxtpzz",
"5-13 r: njrlghrrxfrfv",
"11-14 s: vssnzksspscrss",
"7-10 c: gtrkbcxccccccchch",
"6-11 v: vvsvvvvvvvvvvvvv",
"17-18 b: bbbbbbbqbbbsbbbbsnbb",
"13-15 x: smxxxjxmmkxxxmxx",
"10-11 h: hpqqwkxnfhd",
"15-16 j: jjjjjjjjjjjjzgjjwjjj",
"3-5 f: cjcff",
"3-4 z: hnfzzzmq",
"11-14 c: cccccccccczcckc",
"2-7 t: tstmdtk",
"2-3 f: wffkfm",
"7-16 w: tvgdzjjqlwzknwvwgzh",
"1-2 d: dzdqpn",
"8-14 j: jjzqjxjjsjrngzfj",
"6-9 h: xknzmlzpbpzcth",
"2-5 j: njmnj",
"10-15 z: kfqlljdfzzczzmp",
"7-12 g: gcqwnmgjhcrjnzwcmw",
"3-4 h: hhjhh",
"5-16 d: ddddddvddddddddddd",
"1-2 p: fwwtpllzbmjbwcnkbh",
"10-18 p: vhpwpppxfppppvppdh",
"2-6 x: rqgqgx",
"11-12 m: mhpmmmmmmmmmmm",
"3-4 z: lzzf",
"5-8 w: vfwwmlwfvwwwwlh",
"3-10 t: ltgtztzlct",
"7-8 k: kkkkkkmk",
"10-13 b: ndflbblbchkbq",
"18-19 z: zzzzzzzzzzzzszzzzzzz",
"2-5 n: nlzrmkhz",
"14-15 v: vwvvvvvvvvvjvmcvvv",
"13-15 p: ppppppppwpppxph",
"6-9 k: jvhxzwkkwkzv",
"9-11 s: snspssslkss",
"13-18 j: jgjrjjjjjqjjjhjtjj",
"5-7 v: vgvrhzvvv",
"1-7 t: ttttttttttttt",
"8-9 n: nnnnfnnnj",
"2-5 x: dxcrxhstqwldt",
"6-12 s: dkshssdsltspgcb",
"2-7 k: kkkkkkkk",
"7-13 d: vbjsdddfstdhtdxl",
"12-17 r: nrrgrrsrrrrkrrrdt",
"3-5 w: wwwjw",
"5-8 l: mlfldllll",
"4-5 m: mmmqm",
"9-10 j: sjtmlxjrzl",
"2-14 h: hhhhhhhhhhhhrnhhwh",
"3-4 b: bbbw",
"12-13 g: gggggggggggzg",
"13-14 t: tttgtttrztstltlhb",
"14-17 s: fhdxfshbglsvjsgbs",
"9-13 x: xxxxlxxtxxxxxxx",
"2-3 j: jjtn",
"12-13 n: nnnnnsnwnnvmq",
"3-6 z: gzzzbzmzzzmz",
"3-4 d: ddnt",
"2-7 s: pswmrnsrgb",
"8-9 q: qqqqqqqdv",
"5-6 s: sdlcqs",
"6-10 f: jffwjfhfff",
"4-5 p: pmpppps",
"9-14 p: pppppppppppvpppppppc",
"3-9 n: nsnpnmmnnwtnvb",
"3-4 b: bhzh",
"7-9 g: ggggggggng",
"10-11 x: xwxxxkxxxjxqxxxbbxx",
"17-18 k: kkkkkkkkkkkckkkkkk",
"3-4 v: vvrv",
"12-14 s: vdsrgdsghxcblflbwj",
"8-13 h: gxzhhbkdgfdglfqqcls",
"4-6 m: mmmvmfmmmmm",
"2-13 b: lbtzwffqfrfhbwb",
"1-3 r: lrcr",
"3-6 j: cjtcjj",
"5-8 z: zzztzmzz",
"4-12 t: wttrttvtgttztttdttst",
"6-7 n: zbfvmngknrzfzqpwhtx",
"12-14 g: gggggggggggggbgg",
"6-10 k: jkkkkkrkmbkdh",
"14-19 m: mmmmmmmmmmmmmmmmmmfm",
"2-4 d: sdft",
"4-10 g: bgtgsbjcqgt",
"2-4 t: trtqt",
"7-11 b: wjbbsqsvpkpb",
"12-14 z: zcfqlkxghjjpjzsc",
"3-4 g: ggjt",
"5-7 r: zdrrqrrrrrr",
"15-16 p: brpvpplmhvnbxppc",
"15-16 b: bbxbbbbbbbbbbbbb",
"8-11 c: hscggrpcpbxrxwgsv",
"10-15 j: jjjjjjjjjnjjjjmjjjj",
"4-6 g: bgkghgc",
"9-15 c: ccjcccsbcccspxc",
"2-3 v: fjzb",
"2-3 h: hhhxlchhwmjjzj",
"4-11 x: xxxxlxxxxcxxxxk",
"6-11 d: dvpdmdddzch",
"5-6 j: jjjjjjdjwj",
"6-12 p: pppppxpppppbppp",
"1-7 q: xqqqqqqqqqqqqq",
"5-6 w: xwwrtwjpwgsw",
"11-13 k: kkkkkkkkkkckfkkk",
"2-3 m: qbmnxlwmldmmc",
"2-3 w: jqlwws",
"6-8 k: kkkjbkmz",
"10-12 m: mmmmmmmmmvbm",
"6-13 n: hqnkdmwnxnwndnxgl",
"1-5 j: jjjjb",
"16-17 x: gxxxxxsxxbxxxxxmp",
"3-10 s: ssrsssssss",
"3-4 s: rslpsx",
"1-10 g: qgggjgwqzggvzflmj",
"8-9 g: gggbngqghg",
"1-3 q: qqqfj",
"3-5 m: mmmmzmmmmm",
"7-8 q: qqqxqqgqq",
"1-2 j: rpdjrrt",
"7-10 v: mdzpkvvdpv",
"12-14 m: xzmmjmhmmmmktmtmmmm",
"6-9 m: mmvbmvmzm",
"7-9 c: gcccqmlhc",
"6-8 z: zzzzzznrz",
"4-7 w: wwwmwwww",
"1-4 h: vhhhhh",
"13-14 z: xzzzjzzzzzzfzz",
"1-3 l: jlqml",
"10-12 f: wdbfzsbwffgf",
"4-8 p: vjpppfppxppjmctw",
"18-19 x: zkxbllxbtbzggncfxxx",
"5-6 x: xxxxhxxx",
"2-6 v: tvdprvvrvv",
"5-14 k: jkdhkhdhjgmtkk",
"1-2 k: sskk",
"5-12 w: mvqtkwwmcwwlkw",
"2-6 v: gvmlvv",
"12-13 p: ppppppppppppbp",
"3-4 r: frrrr",
"13-15 r: qrrrrrrrrbrrrrr",
"5-10 b: bxkbrbkdtwwrbkskjpc",
"4-5 x: bxrcx",
"12-15 f: ffffftjfffffffzfff",
"6-7 g: ggggggzgvxggg",
"10-11 w: kgwhvwwwwtcwp",
"9-10 j: jjjjjjjjpjj",
"5-12 t: pnbsttwccrtvttm",
"2-8 c: wcccccxfccnkvrllg",
"2-9 j: frddhfbkkj",
"9-11 m: mmmmmmmmtmmm",
"9-10 m: mmhmmmmmtm",
"2-4 r: crtr",
"14-15 v: vvvvvvvvvvvvvlrv",
"5-6 c: wccwctch",
"1-13 c: lcccccccccccfccc",
"12-15 x: zppxdwxtplfvzfxlwl",
"4-18 c: cccccccccccccccccc",
"2-3 c: xcccc",
"1-7 q: qvfbcfqx",
"6-9 k: lkbkhkkmsjlk",
"7-15 w: wwwwwwwwwwwwrwwwwwww",
"2-5 s: lscsssqsn",
"16-17 n: nnnnnnnnnnnnnnnnznnn",
"4-5 g: ggggggg",
"2-3 w: mfdw",
"4-5 r: rfrqh",
"3-7 f: vfpfbzf",
"8-9 j: jjjjjjjcbj",
"10-13 p: pppppzpppppppp",
"8-10 t: tntbgchftpttttttfttt",
"4-7 r: rlrbsmhnrqrbxrnlrm",
"13-17 m: vkmmmdhfkmtmgmxhk",
"9-11 t: ttttttttttt",
"16-17 g: gggggmgggfgggggsggvg",
"5-7 w: wpffgdw",
"3-7 r: rrzklzbmrrr",
"2-3 l: tllcqnlwfvlfmcgssg",
"3-4 q: qqqp",
"3-7 x: xnxxxzcxrqwx",
"7-18 s: shssssfwssssssksmss",
"1-4 r: rrrrmbc",
"2-6 t: tttdmsmtg",
"3-5 h: tmhbh",
"4-15 c: ccccccccccccccccr",
"8-10 v: vvvkvvvhvk",
"3-6 r: rsmzcrhqnxljrnnd",
"2-3 s: msss",
"10-18 w: wwwwwwwwwwwwwwwwwnw",
"11-13 j: hmwdjqjhjbfdrhj",
"5-17 x: hxpnccxhwlsxxdmxxd",
"4-5 t: ttznj",
"6-7 l: llllllqll",
"1-3 q: qsqnhqm",
"4-6 t: tdtttthc",
"16-17 x: xxxxkxxxxxlmxxvxfx",
"7-11 r: prtrxrprrrrr",
"5-7 j: mjjqjjg",
"3-8 l: rnllnklplllllllll",
"10-15 p: pppppppppdppppp",
"2-6 g: grgggx",
"3-4 s: ssqss",
"1-4 t: tttq",
"6-9 w: fxvvndkmwlskw",
"11-12 c: cccccccccccp",
"4-9 b: bbblbbbbbbbbbb",
"2-3 g: hggnbw",
"17-20 x: xxxpxxxxxxhxxxxxfxxx",
"1-2 f: bpvf",
"3-5 j: wjbfjw",
"13-19 m: srmmmmmmmmfhmgmmmqs",
"10-16 c: cccgcczcccccccbcfcct",
"11-15 b: bzpqpffbfqslknb",
"2-5 t: stnztmvjg",
"3-9 h: hqxhxxhhwh",
"2-4 r: rvrz",
"2-3 p: pppk",
"7-8 s: sskssjdss",
"5-9 x: xzvjjkmqzthpht",
"12-13 p: pstcvcjlnwsqphwnsr",
"3-15 p: lnfhbvnpmfztbqppcf",
"14-18 l: lllljllllllllllgld",
"4-5 g: gctggxhgpxkx",
"7-8 q: qqqqqqrdq",
"10-13 c: ccccccccccccc",
"4-9 s: sssnssskwsbfssssss",
"10-12 g: zgpgghbggjqgggkggjg",
"3-18 m: mmmmmmmmmmmmmmmmmkmm",
"1-3 z: jzzzz",
"1-4 k: fqqwmd",
"4-8 r: wzbrhxrw",
"2-13 x: fzvhrqwcrjjzxprnxlk",
"9-10 q: qqjqqqhqqr",
"4-10 g: mnlggbkdhrgtndk",
"4-19 w: wksmppsqrpppfkdzlrg",
"6-7 k: kkkkkxwkk",
"15-18 t: tttttttttttttthtttt",
"8-13 k: kkkkzkkvkkkktkkk",
"1-5 j: jjlqrwsjzkjbl",
"6-9 m: gmmmdmmmbmmdxmg",
"4-5 r: gdbfmxnrmc",
"3-4 h: rhhhh",
"2-8 n: nnnnnnnln",
"4-9 x: fxgwflwxblgnwxv",
"3-6 x: xmkxxvxxs",
"1-15 g: jgggggpgggggggpg",
"2-7 n: nwnnnnnn",
"2-4 r: hrwcr",
"5-8 x: tbbtxltxdsftztx",
"3-11 r: rzrwrdbqkhrbldrgph",
"2-10 j: jljxrjjxjv",
"17-18 b: bbbbbbwbbbbbbcbbtb",
"10-11 w: wwwjwwwwwrw",
"1-2 h: qbhh",
"2-3 r: rvjr",
"10-13 b: bfbbbjxbbjbbwblc",
"2-4 j: qjdt",
"4-5 j: jjjjjjbfjj",
"11-14 d: pssdgpplqjdzxr",
"4-8 x: zxgxfxjhjxgv",
"6-7 g: gdnhggz",
"3-14 f: fbfffsjffffffgfffff",
"2-7 f: qtxmpvfscrbgxfq",
"6-8 w: wwwwwlqwwswww",
"2-9 g: gbnwwncws",
"1-4 t: ttbctt",
"3-4 g: gggbl",
"5-8 h: hhhhhhhhh",
"9-16 n: nnnnnnnnnnnnnnnnn",
"3-4 x: xxxxxx",
"3-4 l: psgl",
"4-7 p: pppntst",
"4-13 m: mvdmnfnnpxjtmgnwgc",
"9-15 p: pprtppppwnphlhf",
"7-10 v: vlvvbvqtvp",
"11-15 k: jmckdsmvzptdslkkjqf",
"2-3 p: cwkf",
"8-9 r: rrrrmrrhhrr",
"7-8 h: vhhhhhhjh",
"4-5 z: zzhznzk",
"10-13 n: qnnnksnsnvnnnnt",
"1-4 m: jmmmmm",
"5-8 w: jpcmlxtwzvhww",
"10-12 k: kkkkkkkkkkkkk",
"11-14 g: ggggggrgmgggnhgggg",
"1-5 z: zzzwz",
"2-4 x: xxxxxxx",
"6-14 c: cccccvccccccckc",
"11-12 z: zzzkzzbzzcvz",
"13-18 p: pppppppppppppppppxpp",
"9-14 c: tcnphlfkczmcpc",
"7-8 n: wnzmjcnn",
"7-11 p: ppspppmdppp",
"2-6 w: wdwwwww",
"2-4 w: qzvw",
"8-9 j: njbvchssj",
"2-7 b: fnbbbnp",
"3-4 c: ccqv",
"1-5 x: xxqxdxx",
"3-9 w: wzwptwtwwwswbqmk",
"17-18 x: xxhplchxxxxxxxxxgm",
"4-5 g: fsggvmg",
"1-12 w: lwwwwwwwwwwwwwww",
"3-4 b: kbnvg",
"2-7 t: ztttmfftttrtttt",
"2-3 n: wqvnsn",
"1-6 z: qfddndzzg",
"15-17 z: nfzxdmgdvjzzpqdjt",
"1-5 g: mggglgggg",
"5-13 x: xxxxgxxxxxxxrxxb",
"12-13 x: xxxxxxxxxxxcx",
"5-6 r: prrvrrrrh",
"13-14 h: hhhhhhhlhhhhmz",
"8-10 j: jjjjjjnlbjhjzjljj",
"1-7 w: wwwwvwkwwb",
"4-5 h: hpshh",
"2-12 f: vhptghgvhqsf",
"16-17 w: wwwwwwwwwwwwwswzww",
"16-19 x: jltfxxfgkkxnnxjkrxz",
"3-13 s: ssfpvsssshssrxss",
"4-9 q: qsqqrqqqqjkqqkqv",
"9-11 h: djhvttnrjzh",
"2-3 j: jjjz",
"3-7 j: jtjqgmj",
"4-8 p: ppnpcpppspgpc",
"9-13 s: sssskslspdsnss",
"6-10 m: mxzlmmmpvgm",
"10-11 c: cccccccccwnc",
"6-8 f: klkqkthgzfbb",
"7-9 t: tttttttmx",
"2-13 r: nrlmjrhxwnjsrwfx",
"12-13 x: xthxxwpxsdxmj",
"3-11 r: nqgznrmqhcm",
"3-4 c: rqcxmgc",
"12-14 f: ffffffffrdfjffff",
"14-15 d: vdddxdddddddddddd",
"4-8 m: mmmcmkmmmmmkh",
"3-4 g: ggcggsm",
"7-10 p: pppppphppw",
"11-17 f: fffftfxbffffffffrff",
"1-18 f: ffffffffffffffffffff",
"4-6 x: mxnxkx",
"3-7 g: ggrlrmhggl",
"1-2 b: pbblqxtlztwcbt",
"4-5 c: ccccz",
"1-4 k: kqkhkkkk",
"9-12 v: vtvvgvvxvvvvv",
"3-4 g: ncgbnrvdbrm",
"9-12 t: tttttttttttttttt",
"14-17 c: crncccqdsjcclcxcmdw",
"8-10 h: hvhpghvhnfhhh",
"4-12 p: ppplpppppplnpppp",
"4-5 l: lrlllllnlllq",
"3-14 p: ppnppppppppppcpppppp",
"2-5 v: vmvvbv",
"6-7 v: vcvvvqvvvvvjvv",
"4-5 l: llllhl",
"5-12 h: hjhphkxhkcqh",
"6-7 f: fbskrlff",
"4-5 k: rkfnrk",
"1-4 q: tqqkqkqqcxq",
"6-7 p: pppppxp",
"1-2 f: fnfffffffffw",
"5-18 p: ppfpppppppppppppppp",
"1-5 d: dwndd",
"8-9 h: hhhhhhhhh",
"3-6 l: llllllllll",
"9-10 r: gvhwsfbckr",
"7-16 h: hhhhhhhhhhhhhhhhh",
"1-2 j: tjjlj",
"5-9 b: tsvwbmbvbk",
"1-8 r: vrrkbsrrrrkrrcrr",
"1-5 b: hbbbbbs",
"7-8 j: zgjwjcmnjjjljnvjjgj",
"11-15 z: zqzzzxvzzdmzzzzz",
"2-13 q: tqqnzjjxvcsvqksl",
"6-10 f: fqqczfhfmf",
"2-14 v: vcvvvvvvvvvvvvvv",
"1-5 c: kgcdcckbc",
"3-5 r: rrdrr",
"15-16 f: ffffffffffffffmbf",
"10-11 s: ssssssssssssxssnss",
"9-10 j: jjwjjjjjtkj",
"4-5 v: vfdvv",
"2-13 z: znkpztzzzzzzznlwzz",
"3-4 r: lrrm",
"15-16 n: nnnnnnnnnnnnnnsnn",
"6-12 n: nxnnxnnnpnnnnvn",
"4-8 q: lqsqdcqq",
"15-16 x: xxxxxxxxxmxxxxxtxrx",
"6-17 h: hhhhhhhhhhhhpjhhh",
"11-15 c: cccccjccccpcccc",
"11-12 r: rrmrhvzgrtrd",
"3-7 b: bwmbbblb",
"8-13 v: zlvhjhjhtwtkbxqqw",
"6-9 p: pppppfpppppk",
"2-5 r: rcrrjr",
"14-19 f: gfbrfsffprfffhrffzm",
"3-6 r: rrsrrtr",
"4-6 j: jjzjbz",
"1-4 l: jllnl",
"6-7 z: zzzzzppzzzzzz",
"17-18 h: xjvnmlhhnlxltrdltgr",
"2-14 z: xhtwcgngdxlzhnv",
"3-5 v: xvvrvvv",
"11-14 v: dnhpmxjvmwrknvvpr",
"8-17 w: vnwpmbbpmcwwgpwlwh",
"4-5 f: fffjl",
"13-16 v: vzvgvvvwvvvvvvvjvvgk",
"8-9 n: nnnnnknnn",
"18-19 g: gjgggkggggkxgpgdglh",
"2-4 t: ptkzwltkr",
"17-18 q: qbmbqqlqqjqqhtqfqq",
"3-6 r: rfkmhfd",
"4-7 h: fghxhhhh",
"4-5 s: spsxv",
"3-5 k: dkpkzkl",
"7-10 n: nzpnnnlnnsnnn",
"3-4 h: hhnh",
"19-20 r: rsrkmcrhkqfrfdqmlvxq",
"9-10 m: mmhmwmwmmvm",
"3-9 j: jdjjjjbjwjjjjjjjjjj",
"1-2 s: mpsscts",
"3-4 g: nghj",
"6-10 x: xxxxxnxxxhxx",
"10-13 t: tttttttttqttvtttt",
"12-13 s: nssssssnsjrss",
"7-9 z: hjkzxlzrczhhmm",
"16-17 s: sssssssssssssssfpsss",
"4-5 x: xxxxx",
"2-4 c: bppcccfwqs",
"4-11 w: wwwwwwwwwwwkw",
"6-8 m: hdxjhkpjdjmrql",
"2-19 k: zkhcfxztkgltmqbdqxj",
"1-3 n: gnqnnnnnrnnn",
"11-13 f: ffffffffgfmfkf",
"1-5 z: lwzkxzjzv",
"11-12 m: mhlxvjmrcffn",
"2-7 z: cqhbjlbzh",
"3-18 k: kdkkkfbkgwkdknkkkzjk",
"9-10 b: bbrbbbkcbbbbbzll",
"5-6 l: llplkl",
"9-15 c: vcgcngchvkvjsgcf",
"3-6 q: qqqqqwq",
"9-11 k: kxkjrpkkckkkkkskk",
"9-18 k: hbkrrwvctstksttkwrvf",
"2-3 j: jtjj",
"1-5 n: nnnnln",
"1-6 b: jpmbbbbqkd",
"5-7 w: wwkwwws",
"3-10 m: pxpwzblsvrlsxjpvpslt",
"11-12 j: ljjjjkjjjcmc",
"10-11 q: qqqqqqqqqqq",
"2-7 h: hqqhkbh",
"7-9 l: lllclmfslldrlsl",
"8-9 h: jhtvlvrhhhkhh",
"3-6 k: kkjkkkk",
"1-5 l: vllllc",
"1-2 q: vqqq",
"5-6 q: mkqhjp",
"7-14 l: lllllllrdlmlckll",
"3-4 k: kxkkrjk",
"6-8 l: pslrqlbl",
"1-8 t: gtzthtct",
"5-7 d: lhxkdrddf",
"2-3 h: hmhh",
"7-9 p: ppppvppppvwp",
"9-11 q: jhzvqqbqfnql",
"9-14 r: rrrrrrrrtrrrglrrz",
"11-12 s: shsssssssssbs",
"1-7 t: qtttttt",
"11-16 s: spgsmwbrshhldcsvvx",
"5-6 l: lkmlll",
"2-9 h: vdchgpmlhvxzjcp",
"4-7 k: xfkkkkkckmkk",
"1-3 w: wwww",
"13-14 c: cccccccgcwcccxdc",
"12-15 w: wrlwwxwwwlwwwfwcw",
"5-13 m: jmtjqmvkmpxdmt",
"7-11 m: nxnkxfgzcpfm",
"8-10 m: mmmmbhmmmk",
"11-13 z: khcksspxzwmznpl",
"6-7 x: xkxxcxj",
"8-11 s: sssrssssssss",
"6-12 h: wkzcnspbtjwchv",
"8-9 b: bbbbbbbkb",
"7-8 d: hxsjqfddxdb",
"15-16 g: gggggwgggggggggg",
"8-10 q: gqqzqmltqqlkqwtzgfn",
"11-16 j: kjsjjjjjjjckjjjj",
"2-4 s: vbfqcmgssqb",
"16-17 r: rrrrrrrrrrrrrrrrr",
"7-11 d: ddhdddrddtdd",
"2-3 x: gvpcx",
"4-10 t: mbftjndbttv",
"13-14 j: zjjfmsgqtgwdhd",
"6-11 s: qlqhssgsbvnsts",
"9-15 t: ttdttttvttttqttvs",
"3-6 l: lcvlll",
"3-5 x: mpdsxrhqlbcdx",
"1-4 q: kjqz",
"2-3 p: pncmptpppgp",
"2-6 l: tlbvnpllvxlgxhn",
"14-17 q: lgdsvqxwmhdwzhjsq",
"13-19 m: mmmmzmmsmmmmmmmmmmc",
"4-5 x: xxxxzl",
"2-4 n: nnrn",
"8-9 n: nnnnnnnns",
"11-14 l: bpmrcbhslcmxxv",
"7-12 p: ppmpvpppppkpfpp",
"4-10 k: kkkqkkkkkfkkkkk",
"8-11 s: sssfssssnssssss",
"8-16 l: xklrjlllrqlxhrkl",
"2-12 r: rrcrqrprhcrrrvrph",
"14-15 h: jrhhjhhhhhhzhmp",
"8-12 m: mmmmmcmmvwmmx",
"2-9 f: ffdffffmfqpffffffff",
"8-12 x: xxxxxxxgxxxr",
"5-6 z: zzzzzxz",
"14-17 j: jjjjjjjjjjjjjzjjs",
"1-3 f: qfjmrf",
"6-7 t: ttbttdq",
"8-9 x: xfxxxxxxxxbxxxq",
"4-6 q: qqpgwqbr",
"5-12 l: lqzqrtgjmzml",
"5-7 w: wwwnwjwwfw",
"5-6 x: znxdtx",
"4-5 x: qqxhvmxxxxz",
"1-5 n: nnnnnn",
"2-5 s: gxsnj",
"5-7 s: gssjssszst",
"9-14 h: zjhrdpjwhkppdf",
"2-8 t: ftgttpcttxtvnttntjs",
"1-4 t: lttl",
"8-10 f: fffffffffrf",
"3-6 q: qvqxrhd",
"9-10 j: zrfxvmhgzcnkthzs",
"5-7 q: rqtqxqq",
"2-4 j: jxnj",
"7-8 c: fccccczkc",
"1-2 x: xktx",
"5-6 t: tttqkt",
"3-4 m: crbhwmq",
"5-7 d: ddddhdcd",
"3-4 w: wwcn",
"2-7 d: dmdddcd",
"6-7 l: llzllfg",
"5-8 l: llxllllllf",
"3-4 s: lspsb",
"1-6 k: kkkkkdk",
"6-12 x: ztxxmxxqxrxxxcxx",
"5-12 p: fpngpxprbqhprvj",
"1-11 k: kvkkkkkkkkkkkkkkk",
"2-11 x: qxxnxxxxxxxmxfxjsg",
"12-14 r: wzrrfztrbrrrztgrgrm",
"1-4 r: rbrlrj",
"14-16 d: dddddddddddddsddd",
"8-15 l: lzllmllclllljlll",
"7-8 l: qkgqklzzllqclqlfjl",
"1-4 g: vggggg",
"12-13 c: krbpskrctrvtc",
"3-6 t: btttttmkt",
"8-12 t: tttttttttttltttt",
"10-16 k: kkkkkqkkkkkkkkkw",
"5-6 d: ddldvkd",
"10-14 v: vvbrvvvkbvgvvr",
"4-13 v: vvvcvvqcvflrph",
"7-17 x: qxfxxxxvzslqzzbcx",
"9-10 g: ggggggggvjggggggggg",
"3-4 p: hpppkp",
"1-3 s: lstcssssv",
"4-6 n: nnnsnmnnn",
"2-6 k: kkkknkvkg",
"1-2 c: cccccc",
"8-13 h: hhhhhhhhhzhhv",
"10-13 h: hwvhhhhjhhthhhhlxh",
"15-18 p: pzpgpppppgpxpppbppnp",
"10-11 n: nffrjnmbnxj",
"5-9 l: lllldrllbzljsw",
"4-8 j: jjmjjjrjsjjjjj",
"2-9 v: vtzlvvdjv",
"2-3 g: ggcf",
"9-15 b: psxgbbcjbbhbntb",
"15-16 q: qqqqqqqqqqqqqqqz",
"11-12 c: dvgckwdtcccc",
"5-11 s: nskssssssfwb",
"2-7 p: pdfdnpqppzpp",
"3-7 d: dcdwnmdgnstt",
"13-14 w: hwdsrqmdmxhlkm",
"5-7 l: lzzdzlvrtgzllcn",
"5-6 t: bttttvt",
"6-8 c: crcczxckcc",
"5-7 g: gmvgggg",
"7-9 g: gggggglgqgg",
"5-6 t: ttttrt",
"2-3 g: sntggpm",
"4-6 m: flmmsm",
"9-12 w: wwwwwwwwwwjw",
"6-13 x: cfxrwlljbnzlb",
"13-16 v: wvfcgrgfvggjcbqv",
"7-8 n: sdnrsnhn",
"1-3 q: qqqrqmjfq",
"4-6 s: bzdsslss",
"1-5 f: rfffcf",
"4-5 s: sssss",
"4-5 h: xhkhhh",
"10-11 g: ggjdgpvggggx",
"9-10 v: vvvvvvvvjvvvjvwvv",
"3-7 b: fbbmzbblqzvfgpnrl",
"6-11 h: hhhhhlhhhhchhhhh",
"3-4 l: llllstmhwlchzd",
"3-7 t: xthsjgtcblcszn",
"2-17 f: kfjwdtmhzjzlvhpjf",
"2-5 b: rbtbg",
"9-15 z: mzzzcfzzzwvtzqgbzjzm",
"6-12 f: qgtzmktjffmfn",
"11-17 f: flcffsqwlfjvbcffb",
"5-6 r: gsdrrr",
"13-14 b: bbbbbbnbbbnbbbbbsb",
"2-9 b: bcbrvbvbbbzb",
"3-5 t: tkttft",
"6-7 v: vcvlqvdcvdh",
"7-13 w: wwwxwwwwhwwwlqwh",
"5-6 z: zkhpzzjtnkjzf",
"7-9 p: pppppppppppkppppp",
"4-7 p: spppfjmc",
"8-9 k: sxnkplwfz",
"4-5 r: clpgrr",
"7-8 m: mmmntmmmpmmmmrmpk",
"4-5 j: jxbjnxj",
"3-10 b: jwbclnqzdbnb",
"5-6 r: rxbxlnsmrrfr",
"3-4 f: fvfsbq",
"2-4 x: sxxxd",
"7-8 p: qpppppprpp",
"3-4 q: qqqq",
"6-8 n: njwgnqntnnn",
"6-10 z: zdzzgzzzzj",
"6-9 d: rwdlfdrtd",
"5-6 l: skllpxslll",
"5-7 d: dwdznhddttljdnvkdws",
"1-3 d: dhdc",
"1-11 s: sqgzsrrvgms",
"8-14 w: wvvwrwwlwwmwwwn",
"11-12 t: ttbttttttttttttt",
"17-18 f: lfffffmfffffffffkff",
"17-19 k: kkkmzkkkrkfspllkckb",
"4-7 f: fxfjtdfcxff",
"4-10 h: hhhrhhhhhhhhhh",
"6-7 p: ppkpppppp",
"5-10 c: hccpcgbkbctctp",
"5-11 l: llllvljllltlllplll",
"5-6 c: kcntkj",
"16-18 m: mmxmmmmmmmlmmmmwmmm",
"4-7 b: bbvbbrbb",
"6-7 n: dbrqnnn",
"3-4 h: hhhht",
"11-13 s: sssssssssvlwxsfj",
"3-9 g: zrsdrgrzgghxj",
"14-15 f: ffzgnqfrclzgxfffff",
"7-8 c: cccccccbc",
"5-8 s: ssssssssss",
"8-15 k: klkkkppksvdrknd",
"4-6 h: hfhhjljh",
"8-15 c: cxljcccvhpklxcr",
"3-7 h: kpnttrczt",
"14-16 p: tqxpdpddrwfxgjvc",
"12-15 j: cjjjmwjdbtpwjmjcg",
"11-17 n: nnnnnnnnnnnnnnnnln",
"1-8 s: sssswsms",
"9-10 w: wwwwwwwwww",
"6-16 v: gvfjvvvvvqlsbrvvd",
"3-8 q: rvfnrfvsmjk",
"4-6 w: wvpwtww",
"7-10 c: xcctfssplcdqrpqs",
"4-10 j: mjcjjwvjwjm",
"7-11 w: qmwjfrjpjkqww",
"6-18 r: qvvthtbxlkrnvqzvlf",
"10-12 f: ffglffjffffctfffff",
"6-7 x: xxhxtfpqxxx",
"9-10 t: tttttttxtt",
"3-10 j: cpqxwljhgjldfns",
"15-16 q: mqqnqfqjfqqqzqqt",
"4-12 f: fffffffffffvf",
"4-10 s: ssssssszst",
"1-6 x: xgxxxxxxkx",
"2-4 z: zzzb",
"11-13 j: jjjjjjjjjjjjv",
"1-2 j: hjjd",
"4-12 h: hhljhhxhxnhr",
"6-10 b: bbbbbkbbbv",
"7-8 m: mmmmmmgvmm",
"9-15 h: hhhhhhhhwhhhwhhh",
"1-2 g: gvglg",
"4-10 v: gkbvgntvrvv",
"9-10 p: mjpppbppnpjv",
"1-3 w: wwwtww",
"1-7 v: vmvsgjdfdpwtvqqfsh",
"10-12 c: ccccccccclmcccjc",
"13-14 g: gggggglgrggqzgggvbgg",
"1-6 p: mhptnp",
"10-11 n: nnnnnnjnnpxxn",
"2-5 l: tllcc",
"13-14 j: zbvlwljjgljwjj",
"10-11 p: ppppppvpppjppvp",
"12-18 c: cccccccccctdccccch",
"15-16 j: jjjjjjjjjjjjrjjj",
"5-8 t: gjkttztjt",
"5-9 k: kjkhwdvkk",
"5-7 p: pjvpppp",
"2-4 w: wwwhwlwwm",
"4-5 m: mmljm",
"6-15 b: rbbncbrvmdvbbqb",
"13-15 n: nnnrnnpdfnnqnnncnfnn",
"2-11 r: srfhtxczprbx",
"3-6 n: nnnnnh",
"15-16 v: vvvvvrvvvvvvvvvvr",
"7-8 m: jphmmmmft",
"4-6 p: pppjpvp",
"1-4 g: dggkgg",
"1-2 p: zppsp",
"6-7 b: bbbbbbbbbbb",
"3-4 x: vxsv",
"9-13 t: pqtqttttkxtghv",
"10-19 v: vvvvvvvvvvvvvvvvvvxv",
"6-13 z: wnmzkzzqftzmc",
"6-13 l: vklgsrjrkjpzlqll",
"3-6 h: mwhllh",
"1-8 l: blllllltl",
"3-9 v: glxlzpffvgvmb",
"2-5 s: sssstss",
"3-9 t: tfptcrhtlzqxcv",
"9-10 t: ttttttttttjttt",
"9-14 h: ktwphtsnkmlzwd",
"3-5 z: zzznz",
"2-3 t: twtt",
"3-5 f: ffffsf",
"17-18 w: wwhwwwwwvwwwwwwwnsw",
"3-13 w: wwwwwwwvhwwwwpwww",
"7-8 n: pjnxnnnntpwnbsjnnz",
"2-4 v: vvvjhvv",
"2-9 d: dmddwcpnqdddszpb",
"3-4 q: qqrqqh",
"1-2 d: czdd",
"1-4 d: xsdzrms",
"1-3 n: znxnnn",
"5-7 r: rrrrnrzrr",
"2-5 c: ccccxcc",
"6-7 c: nccccdc",
"1-4 s: bslsrvgjdfsgf",
"10-11 j: jcjnjjpjlhh",
"8-12 k: lzrvvhtkkpbkfwjzcmz",
"10-13 b: bbbbbbbrsnbbmb",
"2-9 s: hswtzhlss",
"6-7 j: cpnjjjf",
"11-15 p: pgppqsfjcpbnmqp",
"4-6 k: kkkfwq",
"10-11 c: rccccccccccccc",
"5-14 d: bmfppdgvccmbdqpx",
"7-8 v: vqnvvqvvvvjvv",
"7-16 f: ffffffkfffffffffff",
"14-15 r: nbdlfkrbcrxbcts",
"13-14 v: vvfvvvvvzgvvvvmvv",
"1-12 l: glwdllllpllltll",
"3-9 x: mnxpljmxnm",
"4-5 h: rjqhbxnvkc",
"13-14 z: zzjzkzzlcbzpjzzz",
"2-6 p: tnpppp",
"8-12 n: kpjfjwpnwlzqhwbz",
"2-15 q: jqkjkbzcwvvqbxq",
"2-3 l: llllll",
"15-19 l: llllllllllfllllllll",
"1-3 p: pkzkpsvdptz",
"1-8 f: fffffffvfrf",
"1-11 j: prdqjlhjdvljjvjmhnm",
"10-16 v: stshngzvzvvvnffv",
"10-11 m: nmmtmqmmmmb",
"4-9 t: nzttkfcvrnd",
"18-20 t: bbttltktrgtntgtzhtct",
"4-6 p: pppglp",
"7-13 g: vgrccggpbvxgl",
"5-7 l: lqllvld",
"7-10 w: wswwwwqrww",
"7-8 c: cncczcmlcmcx",
"1-9 d: ggjtdddcqcmpd",
"4-7 q: vdkqwnqkbsdqxwwth",
"5-6 s: ptjwxsz",
"7-14 v: vvgbvtvvxvzvwvvc",
"4-8 h: tmjhhrndwlh",
"6-7 w: wwjvswf",
"2-9 v: vvvvvvvmv",
"2-4 c: hcgc",
"2-3 x: xxxx",
"6-15 h: vnbhwhhwtzztrlh",
"13-16 k: kkknkkkkkkkkkkkrkk",
"2-7 b: nbfxslbqblbbbbbbl",
"9-11 k: kkrqkzkkkvkshqkbkkhk",
"9-13 j: qjjjjjjvmrjjjjjjjj",
"7-15 h: zhqhhhjbhdhhmhfn",
"3-5 t: vtvstkkttftttt",
"7-8 h: hdhhhqhhnnfqwhzhdlsx",
"16-19 k: kkkkkkkkkkkkkkkfkkd",
"3-4 f: qfjsxfnsfq",
"13-14 t: ttjftttcttttptttt",
"8-9 f: gjmfffgrq",
"9-10 m: mmpmmljmmmmmm",
"9-10 k: skttkrjkkb",
"3-4 k: kkgk",
"1-6 h: vhhhhvhh",
"11-19 z: zzhzzzzzzzzvznzzzzgz",
"9-11 z: mzzzzzzlzzbz",
"7-16 c: tpcwtwcbljrnztwrsdd",
"13-15 b: hnrbfgqwqwqhpnc",
"2-4 g: fgsdg",
"2-3 k: kklkkqkhklkkqb",
"8-9 g: tgrfdbvgfzqvsf",
"3-12 j: jmjvwqrpsjvc",
"4-10 v: zvhjvtpjgvvd",
"5-6 p: fgplzd",
"9-13 r: csngrmrxrqvhdwfkvns",
"7-13 q: qqqqqqqqqqqqqqqqq",
"11-16 l: cvlxgkdmltldzsplzz",
"8-11 z: znmhzzcpbzz",
"13-14 x: xxxxxxxxxxxxxhxx",
"11-20 c: qmhcvthqctdtscfcjcck",
"14-15 l: lnllllslwjlllll",
"5-7 p: qppptqm",
"1-7 f: chffvqfrdffbcmqf",
"8-14 h: hhhbhhrshhphhl",
"16-19 j: tgsjqjwjjjbcjtjjjjj",
"3-4 p: jzppdrzpkgcxdljgm",
"5-6 z: zzzzgzzz",
"3-8 t: nvzdttst",
"4-6 x: qfkznxh",
"9-18 d: ddddddddzddddddddl",
"11-17 x: xcxrxxxxxqzrxxxxxxx",
"3-4 l: lmll",
"10-13 f: fffffffffffffff",
"7-9 v: mccgvfvlh",
"9-10 m: ddmlmtmgmmgmprmbmpqm",
"5-10 v: vvvvjvvvvvvvvvx",
"3-10 v: dwxdfjhxgsznhzqsqnd",
"1-3 k: xkrkkkkkkmp",
"2-5 c: dcrscf",
"1-10 p: ppwpwppppppljtppr",
"3-7 r: rrrrrrbrdr",
"5-9 t: ttttjtttttttttt",
"4-5 w: wwwxr",
"6-11 f: rtwzsffhxplnwrzpwwj",
"3-9 c: klcdzfchcnxcccnccpc",
"3-4 g: mgnlg",
"1-5 f: kffgpffft",
"3-4 l: qlsvllnl",
"2-5 w: vwwwwwwrf",
"11-12 n: qcgnnznfnmnt",
"6-13 d: rbbzghqwwmrdkssgn",
"1-3 x: hdxnqxtphtmk",
"10-13 w: xwwwxwcwrfcwm",
"9-10 p: tpppfxvbppppgpnvfzcv",
"8-13 h: nhqhqhthmpmnhlch",
"11-13 z: hjkftzgzlfhjjh",
"9-10 t: tttthttpzt",
"2-8 g: vghggdbfggrfggrgggrt",
"11-16 g: gjzgfnggggsgggzh",
"6-10 r: srmjvrrrlrrrhrl",
"2-11 d: ddddddddbddddd",
"5-6 j: jjfjjjj",
"8-11 s: ssssssssssqssmssss",
"4-5 v: vvvhp",
"5-7 c: ccqxvklbc",
"8-9 q: qnqfgqvqqqdwzqmcq",
"3-5 q: zbqqq",
"6-9 g: kkgzgwpvgt",
"1-14 h: hhhhhhhhhhhhhhh",
"9-10 w: swwwwwwwjq",
"1-13 j: xjwjjljjjjdjjjjmjj",
"11-13 m: smmhmmcmmmkmdmmmmm",
"15-17 p: ppppppppppppppsps"
]

def validate_password1(password, policy):
	match = re.search(r"^(\d+)\-(\d+) (\w)$", policy)
	if match == None:
		raise ValueError("Invalid password policy: " + policy)
	[min, max, letter] = match.groups()
	count = password.count(letter)
	return int(min) <= count and count <= int(max)

def validate_password2(password, policy):
	match = re.search(r"^(\d+)\-(\d+) (\w)$", policy)
	if match == None:
		raise ValueError("Invalid password policy: " + policy)
	[pos1, pos2, letter] = match.groups()
	count = password.count(letter)
	letter1 = password[int(pos1) - 1]
	letter2 = password[int(pos2) - 1]
	return (letter1 != letter2 and (letter1 == letter or letter2 == letter))

valid_count1 = 0
valid_count2 = 0
for policy_password in passwords:
	[policy, password] = policy_password.split(": ")
	if (validate_password1(password, policy)):
		valid_count1 += 1
	if (validate_password2(password, policy)):
		valid_count2 += 1
print("Valid passwords (part one): " + str(valid_count1))
print("Valid passwords (part two): " + str(valid_count2))
