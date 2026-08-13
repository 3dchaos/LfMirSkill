# Mir200 256 Color Reference

## Sources And Confidence

- Primary source: `chm_extracted/256色值.htm`, parsed from each `bgColor=#RRGGBB` cell and its visible number.
- Cross-check source: `knowledge_base/chapters/005-颜色值列表.md`, which preserves the visible number grid but not the HTML background colors.
- Official usage chapters: `knowledge_base/chapters/099-悬浮式装备信息窗口支持图片显示.md`, `838-装备套装备注.md`, `842-自定义属性说明书.md`, `826-悬浮框自定义进度条使用说明.md`, `761-怪物名称颜色自定义功能.md`, and `193-发送屏幕滚动信息.md`.
- Sample evidence: `样本Mir200/Envir/TzItemDescList.txt` uses `223,249` as active/inactive set colors, `116` for set item names, `253`/`56` for set property lines, and `样本Mir200/Envir/ItemDescList.txt` uses `218` broadly for item remarks.

The local HTML contains explicit `bgColor` values for 254 entries. Number `32` has no confirmed cell in either the HTML or Markdown grids; this reference intentionally keeps a `32` row as `source-gap` so the table still spans every numeric ID from `0-255`. Number `255` appears as a visible final cell without `bgColor`; because the cell background is white in the source page and the screenshots, it is recorded as `#FFFFFF` with `inferred-white`.

## Color Usage Rules

- Treat Mir200 colors as numeric palette IDs, not arbitrary RGB values. Script syntax generally expects `0-255` numbers such as `/SCOLOR=250`, `{text|249}`, `SetCustomItemTextColor 1 249`, `SetCustomItemAbil 1 0 0 250`, and `TzItemDescList` rows.
- Prefer official and sample-backed values for player-facing text: `250` bright green for gains/success, `249` red for danger/inactive/warning, `251` yellow for time or headline emphasis, `253` magenta for rare callouts, `254` cyan for readable labels, `116` gold for set/equipment names, and `218` green for item remarks.
- Do not use `32` for new content because the local source skips it. Use nearby warm colors such as `31`, `33`, `34`, or `36` instead.
- Use `255` carefully. It is probably white/default text in the visual table, but the HTML does not declare a `bgColor`; prefer confirmed `246` off-white for white-like text, or use `254` cyan separately when a cool readable label is better than white.
- For inactive states, use strong contrast rather than a dim shade that disappears on dark Mir UI. Sample-backed inactive red `249` is safer than deep reds like `53` or `54`.

## Low-To-High Preset Library

This is a recommended readability/gameplay palette, not an official engine rarity rule. Progression ladder: common -> high -> rare -> epic -> legendary -> mythic -> divine.

| Grade | Main | Accent | Muted/Inactive | Best use |
| --- | --- | --- | --- | --- |
| common | `7` silver | `248` gray | `83` dark gray | ordinary NPC hints, plain material text |
| high | `218` vivid green | `250` pure green | `208` deep green | usable rewards, positive values, item remarks |
| rare | `146` bright cyan | `254` pure cyan | `153` steel blue | systems, labels, readable cool highlights |
| epic | `253` pure magenta | `242` soft purple | `240` muted violet | rare tags, special buttons, magic effects |
| legendary | `116` gold | `251` pure yellow | `108` ochre | equipment names, set names, premium currency |
| mythic | `249` pure red | `58` vivid red | `55` dark red | boss warnings, danger, failed or inactive state |
| divine | `246` ivory | `255` inferred white | `100` parchment | sacred/ultimate text, final-tier title contrast |

Recommended pairings:

| Scenario | Primary | Secondary | Warning/Inactive | Example pattern |
| --- | --- | --- | --- | --- |
| Item remark | `218` | `250` | `249` | `物品名=218/说明\250/收益{+10%|250}` |
| Set remark | `223` active green | `116` gold item names | `249` inactive red | `223,249/套装名|2|116/装备名:253/属性{+15%|250}` |
| Boss notice | `249` | `251` | `55` | `{【世界BOSS】:/SCOLOR=249}{怪物名/SCOLOR=251}` |
| Success notice | `250` | `254` | `248` | `{成功/SCOLOR=250}{目标/SCOLOR=254}` |
| Timer/activity | `251` | `70` orange | `248` | `{限时活动/SCOLOR=251}` |
| Custom item text | `146` | `250` | `249` | `SetCustomItemTextColor 4 146` plus green/red property values |
| Custom attribute | `250` | `249` | `248` | `SetCustomItemAbil 1 0 0 250` for positive lines |
| Low-key admin/debug | `248` | `254` | `249` | keep diagnostics readable without looking like player reward text |

## Full Palette Table

| ID | Hex | Cue | Notes |
| --- | --- | --- | --- |
| 0 | #000000 | black | pure black |
| 1 | #800000 | dark-red | base dark red |
| 2 | #008000 | dark-green | base dark green |
| 3 | #808000 | olive | base olive |
| 4 | #000080 | dark-blue | base dark blue |
| 5 | #800080 | purple | base purple |
| 6 | #008080 | teal | base teal |
| 7 | #C0C0C0 | silver | common/light neutral |
| 8 | #558097 | slate-blue | muted blue gray |
| 9 | #9DB9C8 | pale-blue | light blue gray |
| 10 | #7B7373 | warm-gray | muted warm gray |
| 11 | #2D2929 | charcoal | dark neutral |
| 12 | #5A5252 | dark-warm-gray | dark neutral |
| 13 | #635A5A | warm-gray | muted neutral |
| 14 | #423939 | dark-brown-gray | dark neutral |
| 15 | #1D1818 | near-black-red | very dark |
| 16 | #181010 | near-black-red | very dark |
| 17 | #291818 | dark-maroon | very dark red |
| 18 | #100808 | near-black | very dark |
| 19 | #F27971 | salmon | light red |
| 20 | #E1675F | coral-red | light red |
| 21 | #FF5A5A | bright-red | warning accent |
| 22 | #FF3131 | vivid-red | strong warning |
| 23 | #D65A52 | muted-red | warm red |
| 24 | #941000 | blood-red | dark red |
| 25 | #942918 | brick-red | dark red |
| 26 | #390800 | deep-brown-red | very dark red |
| 27 | #731000 | dark-red | dark red |
| 28 | #B51800 | strong-red | warning |
| 29 | #BD6352 | clay-red | muted red |
| 30 | #421810 | dark-brown-red | very dark warm |
| 31 | #FFAA99 | peach | pale red |
| 32 | n/a | source-gap | missing from local HTML and Markdown grids; avoid for new scripts |
| 33 | #733929 | brown-red | warm brown |
| 34 | #A54A31 | burnt-orange | warm brown |
| 35 | #947B73 | taupe | muted neutral |
| 36 | #BD5231 | orange-red | warm highlight |
| 37 | #522110 | dark-brown | warm dark |
| 38 | #7B3118 | brown | warm brown |
| 39 | #2D1810 | dark-brown | very dark warm |
| 40 | #8C4A31 | brown | warm brown |
| 41 | #942900 | dark-orange-red | strong warm |
| 42 | #BD3100 | orange-red | strong warm |
| 43 | #C67352 | clay-orange | warm highlight |
| 44 | #6B3118 | brown | warm brown |
| 45 | #C66B42 | orange-brown | warm highlight |
| 46 | #CE4A00 | orange-red | strong orange |
| 47 | #A56339 | copper | warm brown |
| 48 | #5A3118 | brown | dark warm |
| 49 | #2A1000 | near-black-brown | very dark |
| 50 | #150800 | near-black-brown | very dark |
| 51 | #3A1800 | deep-brown | very dark |
| 52 | #080000 | near-black-red | very dark |
| 53 | #290000 | deep-maroon | very dark red |
| 54 | #4A0000 | dark-maroon | very dark red |
| 55 | #9D0000 | dark-red | inactive/danger variant |
| 56 | #DC0000 | bright-red | sample set property color |
| 57 | #DE0000 | bright-red | red highlight |
| 58 | #FB0000 | vivid-red | strong red |
| 59 | #9C7352 | tan-brown | muted warm |
| 60 | #946B4A | tan-brown | muted warm |
| 61 | #734A29 | brown | muted warm |
| 62 | #523118 | dark-brown | dark warm |
| 63 | #8C4A18 | orange-brown | warm |
| 64 | #884411 | brown-orange | warm |
| 65 | #4A2100 | deep-brown | very dark warm |
| 66 | #211810 | near-black-brown | very dark |
| 67 | #D6945A | tan-orange | warm highlight |
| 68 | #C66B21 | orange-brown | warm highlight |
| 69 | #EF6B00 | bright-orange | strong warm |
| 70 | #FF7700 | vivid-orange | activity/header accent |
| 71 | #A59484 | beige-gray | muted neutral |
| 72 | #423121 | dark-brown | dark warm |
| 73 | #181008 | near-black-brown | very dark |
| 74 | #291808 | deep-brown | very dark |
| 75 | #211000 | deep-brown | very dark |
| 76 | #392918 | dark-brown | dark warm |
| 77 | #8C6339 | bronze | muted gold-brown |
| 78 | #422910 | dark-brown | dark warm |
| 79 | #6B4218 | brown | muted warm |
| 80 | #7B4A18 | brown-orange | muted warm |
| 81 | #944A00 | orange-brown | warm |
| 82 | #8C847B | gray-beige | neutral |
| 83 | #6B635A | dark-gray | muted/inactive neutral |
| 84 | #4A4239 | charcoal-brown | dark neutral |
| 85 | #292118 | dark-brown-gray | very dark |
| 86 | #463929 | dark-taupe | dark neutral |
| 87 | #B5A594 | beige | light neutral |
| 88 | #7B6B5A | taupe | muted neutral |
| 89 | #CEB194 | sand | light warm |
| 90 | #A58C73 | tan | muted warm |
| 91 | #8C735A | tan-brown | muted warm |
| 92 | #B59473 | tan | light warm |
| 93 | #D6A573 | light-orange | warm highlight |
| 94 | #EFA54A | amber | gold-orange |
| 95 | #EFC68C | light-gold | warm light |
| 96 | #7B6342 | olive-brown | muted warm |
| 97 | #6B5639 | brown | muted warm |
| 98 | #BD945A | bronze | warm gold |
| 99 | #633900 | dark-bronze | dark gold |
| 100 | #D6C6AD | parchment | divine muted text |
| 101 | #524229 | dark-olive-brown | dark warm |
| 102 | #946318 | bronze | warm gold |
| 103 | #EFD6AD | pale-gold | light warm |
| 104 | #A58C63 | antique-gold | muted gold |
| 105 | #635A4A | olive-gray | muted neutral |
| 106 | #BDA57B | antique-gold | muted gold |
| 107 | #5A4218 | dark-bronze | dark gold |
| 108 | #BD8C31 | ochre | muted legendary |
| 109 | #353129 | charcoal | dark neutral |
| 110 | #948463 | muted-gold-gray | neutral |
| 111 | #7B6B4A | olive-brown | neutral |
| 112 | #A58C5A | dull-gold | muted gold |
| 113 | #5A4A29 | dark-olive | dark gold |
| 114 | #9C7B39 | bronze | gold-brown |
| 115 | #423110 | dark-gold-brown | dark warm |
| 116 | #EFAD21 | gold | sample equipment/set-name gold |
| 117 | #181000 | near-black-gold | very dark |
| 118 | #292100 | deep-olive | very dark gold |
| 119 | #9C6B00 | dark-gold | muted gold |
| 120 | #94845A | antique-gold | muted gold |
| 121 | #524218 | dark-olive | dark gold |
| 122 | #6B5A29 | olive-gold | muted gold |
| 123 | #7B6321 | bronze | muted gold |
| 124 | #9C7B21 | gold-brown | muted gold |
| 125 | #DEA500 | bright-gold | gold highlight |
| 126 | #5A5239 | olive-gray | muted neutral |
| 127 | #312910 | dark-olive | very dark |
| 128 | #CEBD7B | pale-gold | light gold |
| 129 | #635A39 | olive-gray | muted neutral |
| 130 | #94844A | antique-gold | muted gold |
| 131 | #C6A529 | gold | gold highlight |
| 132 | #109C18 | green | strong green |
| 133 | #428C4A | muted-green | muted green |
| 134 | #318C42 | muted-green | muted green |
| 135 | #109429 | green | strong green |
| 136 | #081810 | near-black-green | very dark |
| 137 | #081818 | near-black-teal | very dark |
| 138 | #082910 | deep-green | very dark |
| 139 | #184229 | dark-green | dark green |
| 140 | #A5B5AD | pale-green-gray | light neutral |
| 141 | #6B7373 | gray-teal | muted neutral |
| 142 | #182929 | dark-teal | dark cool |
| 143 | #18424A | dark-cyan | dark cool |
| 144 | #31424A | blue-gray | dark cool |
| 145 | #63C6DE | cyan-blue | cool highlight |
| 146 | #44DDFF | bright-cyan | readable system highlight |
| 147 | #8CD6EF | light-cyan | cool light |
| 148 | #736B39 | olive | muted olive |
| 149 | #F7DE39 | bright-yellow | yellow highlight |
| 150 | #F7EF8C | pale-yellow | light yellow |
| 151 | #F7E700 | vivid-yellow | strong yellow |
| 152 | #6B6B5A | olive-gray | muted neutral |
| 153 | #5A8CA5 | steel-blue | rare muted |
| 154 | #39B5EF | sky-blue | cool highlight |
| 155 | #4A9CCE | blue | cool highlight |
| 156 | #3184B5 | blue | cool |
| 157 | #31526B | dark-blue-gray | dark cool |
| 158 | #DEDED6 | light-gray | readable neutral |
| 159 | #BDBDB5 | silver-gray | neutral |
| 160 | #8C8C84 | gray | neutral |
| 161 | #F7F7DE | ivory | soft light |
| 162 | #000818 | near-black-blue | very dark |
| 163 | #081839 | navy | very dark blue |
| 164 | #081029 | dark-navy | very dark blue |
| 165 | #081800 | near-black-green | very dark |
| 166 | #082900 | deep-green | very dark green |
| 167 | #0052A5 | blue | saturated blue |
| 168 | #007BDE | bright-blue | blue highlight |
| 169 | #10294A | navy | dark blue |
| 170 | #10396B | dark-blue | dark blue |
| 171 | #10528C | blue | muted blue |
| 172 | #215AA5 | blue | cool |
| 173 | #10315A | navy | dark blue |
| 174 | #104284 | blue | cool |
| 175 | #315284 | blue-gray | muted blue |
| 176 | #182131 | dark-blue-gray | very dark |
| 177 | #4A5A7B | slate-blue | muted blue |
| 178 | #526BA5 | blue-gray | muted blue |
| 179 | #293963 | navy | dark blue |
| 180 | #104ADE | vivid-blue | strong blue |
| 181 | #292921 | dark-olive-gray | very dark |
| 182 | #4A4A39 | olive-gray | dark neutral |
| 183 | #292918 | dark-olive | very dark |
| 184 | #4A4A29 | olive | dark muted |
| 185 | #7B7B42 | olive | muted olive |
| 186 | #9C9C4A | yellow-olive | muted yellow |
| 187 | #5A5A29 | dark-olive | muted |
| 188 | #424214 | dark-olive | dark |
| 189 | #393900 | dark-olive | dark |
| 190 | #595900 | olive | dark |
| 191 | #CA352C | red | warm red |
| 192 | #6B7321 | olive-green | muted green |
| 193 | #293100 | deep-olive | very dark |
| 194 | #313910 | dark-olive | dark |
| 195 | #313918 | dark-olive | dark |
| 196 | #424A00 | olive | dark |
| 197 | #526318 | olive-green | muted green |
| 198 | #5A7329 | olive-green | muted green |
| 199 | #314A18 | dark-green | dark green |
| 200 | #182100 | near-black-green | very dark |
| 201 | #183100 | deep-green | very dark |
| 202 | #183910 | dark-green | dark green |
| 203 | #63844A | muted-green | green neutral |
| 204 | #6BBD4A | light-green | positive |
| 205 | #63B54A | green | positive |
| 206 | #63BD4A | green | positive |
| 207 | #5A9C4A | muted-green | positive muted |
| 208 | #4A8C39 | deep-green | muted positive |
| 209 | #63C64A | bright-green | positive |
| 210 | #63D64A | bright-green | positive |
| 211 | #52844A | muted-green | muted |
| 212 | #317329 | dark-green | dark |
| 213 | #63C65A | green | positive |
| 214 | #52BD4A | green | positive |
| 215 | #10FF00 | neon-green | very bright positive |
| 216 | #182918 | dark-green-gray | very dark |
| 217 | #4A884A | muted-green | green |
| 218 | #4AE74A | vivid-green | common item remark color |
| 219 | #005A00 | dark-green | guild/sample green variant |
| 220 | #008800 | green | strong green |
| 221 | #009400 | green | strong green |
| 222 | #00DE00 | bright-green | positive |
| 223 | #00EE00 | active-green | sample active set color |
| 224 | #00FB00 | vivid-green | positive |
| 225 | #4A5A94 | slate-blue | muted blue |
| 226 | #6373B5 | periwinkle | blue-purple |
| 227 | #7B8CD6 | light-blue | cool light |
| 228 | #6B7BD6 | blue-purple | cool |
| 229 | #7788FF | bright-blue | cool highlight |
| 230 | #C6C6CE | light-gray | readable neutral |
| 231 | #94949C | gray | neutral |
| 232 | #9C94C6 | lavender-gray | muted purple |
| 233 | #313139 | charcoal-purple | dark neutral |
| 234 | #291884 | deep-purple | dark magic |
| 235 | #180084 | deep-blue-purple | dark magic |
| 236 | #4A4252 | purple-gray | muted |
| 237 | #52427B | muted-purple | magic muted |
| 238 | #635A73 | lavender-gray | muted purple |
| 239 | #CEB5F7 | pale-purple | epic light |
| 240 | #8C7B9C | muted-violet | epic muted |
| 241 | #7722CC | vivid-purple | epic |
| 242 | #DDAAFF | soft-purple | epic accent |
| 243 | #F0B42A | orange-gold | premium/event accent |
| 244 | #DF009F | hot-magenta | strong epic |
| 245 | #E317B3 | magenta | strong epic |
| 246 | #FFFBF0 | ivory | confirmed near-white |
| 247 | #A0A0A4 | gray | neutral |
| 248 | #808080 | gray | muted/inactive neutral |
| 249 | #FF0000 | pure-red | sample inactive/danger/boss color |
| 250 | #00FF00 | pure-green | sample success/positive color |
| 251 | #FFFF00 | pure-yellow | headline/time/activity color |
| 252 | #0000FF | pure-blue | pure blue |
| 253 | #FF00FF | pure-magenta | rare/callout color |
| 254 | #00FFFF | pure-cyan | readable label color |
| 255 | #FFFFFF | inferred-white | final white cell has no HTML bgColor; use carefully |
