#
# [794] Swim in Rising Water
#
# https://leetcode.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (45.49%)
# Total Accepted:    8.7K
# Total Submissions: 19.1K
# Testcase Example:  '[[0,2],[1,3]]'
#
# On an N x N grid, each square grid[i][j] represents the elevation at that
# point (i,j).
# 
# Now rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and
# only if the elevation of both squares individually are at most t. You can
# swim infinite distance in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.
# 
# You start at the top left square (0, 0). What is the least time until you can
# reach the bottom right square (N-1, N-1)?
# 
# Example 1:
# 
# 
# Input: [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a
# higher elevation than t = 0.
# 
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# 
# 
# Example 2:
# 
# 
# Input:
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation:
# ⁠0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
# 
# The final route is marked in bold.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
# 
# 
# Note:
# 
# 
# 2 <= N <= 50.
# grid[i][j] is a permutation of [0, ..., N*N - 1].
# 
# 
#
from heapq import *
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ret = 0
        visited = [[False] * N for i in xrange(N)]
        h = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        while not visited[-1][-1]:
            t, i, j = heappop(h)
            ret = max(ret, grid[i][j])
            visited[i][j] = True
            for i, j in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and not visited[i][j]:
                    heappush(h, (grid[i][j], i, j))
        return ret

    def test(self):
        #print self.swimInWater([[0,2],[1,3]])
        #print self.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
        print self.swimInWater([[1965,1760,1509,150,875,1812,791,320,1100,322,1491,2445,49,1492,1764,861,749,395,560,2012,1906,1085,511,1342,1847,1088,2083,781,269,2322,541,792,639,730,1480,1280,1411,241,885,72,1322,1903,232,1249,310,777,1319,2044,1267,762],[1824,810,769,1678,2097,1286,2421,667,2181,293,1412,2199,1424,1556,1536,2157,563,794,873,1967,830,2169,683,1175,450,1339,2466,1604,1096,1934,756,1224,682,1364,2366,1995,947,2029,2114,835,2496,513,2401,82,2441,1755,195,1980,1435,950],[1346,606,738,1365,989,277,2196,2094,2033,1349,2076,812,397,1644,2216,2050,515,1654,1730,439,1618,347,1511,1470,2160,1450,816,1036,2081,2316,365,974,2327,1710,2480,1720,224,622,34,1701,420,354,1202,1247,1483,1853,962,1116,815,1698],[933,81,1417,1300,1653,237,774,1426,1165,636,1549,806,954,1723,905,267,1484,1968,870,1051,1472,1962,967,959,712,311,2397,614,707,1708,1140,1153,2288,2436,128,509,27,451,1157,2499,487,1262,1766,10,1560,12,343,172,440,1335],[2207,1904,387,1552,91,2104,2195,1827,461,389,808,24,182,650,2043,2124,840,459,1510,2233,355,2309,1399,2380,2021,708,73,2166,1524,1783,690,1794,1987,93,1434,2161,2394,2308,1646,1855,1161,488,2349,1807,1131,1888,3,1774,1473,697],[2209,84,1664,2245,2149,925,605,2374,39,1716,1554,1744,976,1135,1028,886,995,1406,69,60,486,558,1494,1064,2075,266,1113,704,2486,1874,1981,164,2226,1568,1615,2460,2218,587,1334,2473,923,1385,1836,223,2120,522,2208,2492,1284,2274],[197,548,18,1059,1297,1039,8,2001,1160,765,2312,1999,20,673,1327,263,1027,176,2092,1834,1205,1809,671,540,1301,2452,2234,1884,1731,1299,956,768,97,1151,1638,479,878,2193,1625,864,1605,1210,2287,490,1138,1845,41,720,1239,1168],[1132,2167,579,1078,358,1102,653,315,1108,2352,1758,740,2155,834,2495,1801,507,844,1370,1515,2439,296,2357,675,2132,2293,1666,573,437,780,1079,635,824,797,1049,1797,1486,1456,2494,1911,1092,1645,747,1652,2112,1076,607,2096,494,2156],[2103,1268,2468,1905,2388,1067,1671,1883,872,1837,1001,1960,805,1360,408,1199,1101,700,1831,793,125,2365,965,503,644,1008,1547,2093,280,288,71,1691,935,1179,2296,392,1014,2227,1155,940,2475,1912,1818,732,467,2359,2416,213,1498,1263],[601,1242,481,681,1875,693,1879,1240,930,2134,115,2128,865,1081,2017,941,629,743,282,285,2387,570,2214,359,380,2260,1419,1662,2393,1627,831,1839,292,228,2268,1614,53,158,1381,2009,814,270,2371,325,1139,1640,630,151,1863,1639],[1799,891,2448,2246,1581,591,2041,1441,666,2457,1806,801,1219,333,168,1089,2253,1754,326,368,764,526,391,820,1947,2278,448,388,2063,1469,1979,2377,1221,921,413,2498,2392,407,1338,1376,2205,643,1006,246,1257,754,435,1442,964,1679],[1474,2170,239,741,2172,2144,1225,2426,2109,983,532,472,1986,977,1368,2212,646,177,1856,1350,430,785,1878,2018,1272,26,1055,1216,1916,843,1358,1195,1548,47,1061,2491,308,2242,426,2477,1894,133,1562,1333,159,468,52,1741,2258,297],[1748,552,186,2485,1540,615,1739,2147,902,204,1002,1166,1330,1842,981,1276,2262,616,1455,1026,2224,330,1206,1261,1340,2176,1180,1682,2271,857,523,1609,312,372,800,427,2459,543,1506,2153,279,229,2102,32,1535,1572,1543,222,1829,250],[2022,278,2243,445,854,2405,617,819,717,1389,779,2476,679,1707,1606,1954,2194,42,417,1375,167,680,1964,165,2396,1444,454,1,398,2056,1173,1366,877,939,1405,838,1029,2399,1192,842,1136,2184,678,1593,1143,2273,37,2072,772,480],[46,499,836,771,1957,1715,1071,1635,1533,2272,869,15,2091,1914,1269,139,1147,937,2417,136,710,858,1918,188,163,1815,221,1559,1214,361,914,1601,2490,356,1961,187,994,1391,2434,429,888,2442,1923,386,1171,1558,363,1120,758,2345],[1416,2101,1514,2151,1932,1505,2254,2433,978,1174,1681,850,1044,1213,1243,227,2303,1105,776,2086,604,1997,121,1274,2126,2267,196,1060,50,569,412,1712,152,652,2276,893,1082,528,1040,1687,581,2376,2307,1550,1030,542,1531,624,966,715],[286,130,2435,419,1870,1305,2311,337,2497,1445,1022,7,833,462,953,1018,1767,1197,452,1935,1394,1181,1227,1194,1594,2002,1538,463,567,901,519,1032,2116,1091,716,1576,2028,868,1940,2139,2127,656,1602,1972,1150,884,1672,1649,948,2256],[2141,1570,782,2175,766,2385,1503,1711,912,1529,1919,2454,859,2429,5,1742,1564,2131,1527,1244,1899,318,148,1545,1889,1024,86,1065,2282,1686,1402,111,1613,65,1589,1886,57,1009,1890,752,927,2215,103,1198,2302,105,651,1403,2058,1077],[220,1468,735,1746,517,317,495,2446,1785,951,1314,2384,1530,1308,1661,1597,1948,1588,1791,1551,1603,546,1823,1427,555,1990,2318,353,1201,1953,199,113,1740,319,922,934,2162,904,1811,2361,2339,1753,262,1788,2237,1489,443,2304,993,256],[449,1717,1343,799,2464,2121,1665,719,1838,146,1252,637,376,1828,2206,1873,33,2190,562,1204,1279,553,1121,1072,2406,883,1683,518,1066,1248,2106,2414,589,2171,2099,755,1526,500,778,2025,970,1271,1575,1073,1969,1306,301,30,2450,1184],[1388,525,110,418,13,2231,660,2174,1062,2378,691,1880,915,1695,584,811,2222,2364,120,999,920,2281,1212,2289,88,1773,1084,92,647,1541,21,1584,2164,582,1003,788,1045,1144,841,2348,129,1176,961,1629,1591,1632,1090,1861,600,396],[1465,1643,162,1843,1745,1476,145,245,1291,2015,1893,1410,1620,1058,1925,672,160,1810,1464,1743,596,1805,1260,860,0,1702,2154,484,373,2057,284,174,975,254,316,2210,1080,658,1190,1718,29,1699,300,1451,1222,302,547,77,126,75],[619,191,2200,1446,986,236,1460,1553,1616,2470,2105,837,1583,1454,1229,2,1236,19,2315,1007,1430,1241,1196,1881,2005,721,620,66,2204,1737,1193,847,1930,1428,1378,963,1458,1422,1963,898,161,2358,1234,1867,1104,856,2090,1813,109,2073],[456,2059,597,1516,122,1336,2409,2223,2368,1125,411,786,817,2239,968,2061,1704,2007,431,59,332,588,492,2337,1958,1630,760,2046,424,1420,1017,1466,1507,1587,1941,502,1566,38,1270,1109,305,784,911,313,294,2320,1780,1825,909,2355],[1993,43,2000,99,1705,1610,478,2482,209,608,1490,1778,602,446,1714,143,2375,2389,212,2301,1277,1532,67,676,1577,2250,1348,2261,1282,598,1633,1738,138,1528,2427,2335,489,568,2136,1145,265,2295,1183,1288,1765,988,1826,1471,711,689],[1152,2330,428,1749,1114,1390,238,832,1719,1959,742,2465,444,2251,1798,2236,1944,2391,1035,153,1822,1386,1728,1215,1320,314,1200,1667,829,1895,140,2030,809,1048,471,692,2266,1668,1877,2411,2381,460,1265,508,1123,688,750,621,972,1795],[1951,1031,1086,2168,35,633,2045,1908,881,1487,1887,1070,1751,2088,231,1992,1634,493,594,1034,1596,1438,1361,1010,1437,529,2008,276,664,1397,78,612,1871,107,1355,938,1574,1129,11,309,640,1186,980,1409,1273,1037,299,659,2024,846],[1660,1571,1285,2027,1344,244,2019,1337,2040,645,1369,2438,1771,382,1046,1429,1781,603,2125,1859,423,2407,249,211,1840,175,2440,734,2471,714,1900,916,216,2323,2300,1413,123,137,1858,477,578,258,1298,16,946,928,2319,1142,225,1846],[577,524,2082,1607,1976,233,394,642,1563,839,2183,339,2034,40,1804,2347,1736,1053,2107,1148,787,1835,367,2182,1713,1833,142,2277,1485,926,217,2165,1926,2111,1910,1869,1041,1068,634,1696,2163,1647,2039,352,70,2148,416,897,2419,1156],[2362,1134,802,1384,1452,275,1374,586,1264,2159,1542,1309,566,1776,1623,2336,501,1612,718,1371,2493,74,731,1401,1817,737,907,287,1303,890,632,917,334,1557,1688,2179,1163,385,1278,1170,2186,2071,432,2428,1396,1057,102,798,867,2213],[1289,321,2390,1952,1033,4,1814,1709,1585,379,1118,2333,706,264,1021,2197,1347,497,2037,2064,1325,80,447,1432,1513,1130,906,210,31,304,1546,1921,1657,1891,1256,200,1502,534,2062,894,179,698,171,1988,89,1966,572,1387,252,1185],[1162,1852,1659,1245,2294,399,1115,2095,58,723,208,2173,2026,549,559,2467,1539,340,327,2342,455,1328,2410,384,234,985,1898,2244,1772,1848,2474,2143,118,247,733,851,627,2346,882,1885,726,853,98,2023,705,351,1407,51,218,2283],[845,1133,1351,1025,1586,226,1019,1323,818,2247,520,514,1816,201,1477,1357,918,2356,1866,2370,2279,2284,2074,2324,1901,2054,1628,474,496,470,574,1255,190,895,1016,1107,1611,971,1685,1447,1724,1522,623,2013,694,695,324,1786,1418,2422],[1141,1482,1750,531,1063,2006,2130,1218,260,1087,1650,1254,669,198,364,189,1722,366,2068,1158,303,1020,1567,2447,996,2463,1676,1207,2016,770,56,1117,931,1475,1208,1882,1359,203,1850,852,268,2372,2192,1619,390,551,804,655,575,2408],[283,638,2328,1253,307,1421,2270,2329,180,2229,2444,2202,1250,2014,2395,1321,2257,1631,2189,465,1656,505,1565,2402,1844,2069,1534,76,1775,64,828,2185,1052,960,1770,593,378,2403,2078,1311,992,1383,2220,1111,1235,2115,557,1312,1949,1677],[1443,498,1841,2310,2430,144,1042,2481,1501,1425,2264,1978,1356,255,94,1228,744,746,2203,2350,1955,1796,1172,1924,90,2425,192,751,393,2479,1977,631,2122,1590,862,874,402,957,1518,2367,207,1362,1519,1392,1820,556,866,2238,1998,1266],[406,1872,1670,2343,1404,2321,2484,1680,2221,641,1789,441,1395,1128,1345,1768,871,485,1803,2313,1669,504,350,1599,491,1937,998,1281,663,1971,83,2241,2269,2332,1927,1726,1038,1782,997,1994,2443,178,987,1641,984,668,684,2420,273,2158],[2201,1922,713,2065,344,1433,2089,135,510,2291,272,1182,2031,2404,2462,1703,1876,813,1341,1651,1759,1920,127,1950,1508,611,1849,68,2478,1697,1497,2340,1154,1648,2483,184,1226,2360,1808,1942,903,346,243,1595,1463,63,662,173,1608,466],[2338,409,2341,2248,349,2129,576,783,295,1467,2451,483,1757,2235,1496,1423,1865,2198,422,1956,2133,1304,1232,205,1146,887,1440,1187,701,1103,1149,401,48,512,1500,2415,757,369,991,95,147,739,2117,1188,1800,2048,1295,855,973,1448],[290,2252,1379,796,2353,331,149,6,657,2334,1762,1819,1373,1857,2070,709,2042,2325,289,2077,1495,908,561,1733,609,1939,1178,554,215,979,1095,251,879,360,722,1929,1555,539,362,117,565,544,2423,1363,383,2299,87,1642,404,982],[823,370,1177,405,1488,2487,25,803,261,54,329,2191,1851,2472,1544,2437,1317,2067,61,876,2038,2488,2286,1159,535,132,1915,1352,1673,932,1098,530,2305,119,2110,2424,2232,1725,1307,338,2379,1689,2032,618,374,1127,235,949,345,969],[1694,1122,79,696,1938,1784,2138,206,157,1729,1982,2461,410,1569,1318,1283,85,14,724,1315,1517,1293,2100,729,1892,291,1258,1663,1727,1864,585,2047,1191,240,550,1050,1251,537,341,1097,1012,62,1296,1592,2314,1860,1093,1436,1655,2292],[1624,825,516,1537,1354,2285,1238,55,23,2297,2211,1004,108,1973,473,699,728,889,2010,725,913,44,1461,2135,415,610,1013,807,2180,2383,194,166,1459,654,1523,114,469,648,1933,2178,1830,1310,1520,230,1792,1675,1521,28,748,1453],[2373,1011,438,9,248,944,1015,1431,242,1217,328,377,2035,214,442,457,2259,1329,2240,453,1561,2113,1124,1600,2066,281,1769,1580,538,1237,1302,1000,703,2098,2412,1316,2326,1974,2087,1573,1578,955,892,1499,2413,2052,323,2004,1074,665],[2298,2455,2275,1209,1747,155,348,687,1449,702,2489,1996,433,2398,2351,1457,1112,863,1005,775,2386,2085,96,1761,736,521,1462,2011,2230,124,1582,2280,590,2053,599,1246,790,1931,849,298,1382,649,1622,1167,880,795,919,1943,1598,371],[2119,1069,1970,1793,1231,789,2382,685,821,1637,2145,1353,2363,506,2188,1579,342,1099,2187,625,2306,2123,1439,1292,571,1169,17,1230,759,1056,1380,1189,2354,134,436,1991,1693,1294,527,1400,1203,106,896,1290,670,592,900,674,1137,154],[1617,1756,458,1928,943,100,1372,1821,170,1802,686,2265,336,2249,2290,1983,2118,677,2469,1690,1790,2080,628,2137,104,2049,2418,1700,1504,1054,421,2225,1621,1324,141,753,1259,335,1393,626,1692,375,2400,425,1094,2051,1946,2152,101,271],[2060,1479,1478,2142,2146,1106,476,1415,1408,274,1896,400,826,131,1936,1732,1233,595,156,2317,936,952,1119,1110,2036,1083,1275,945,1902,1907,1636,1913,1512,257,1735,1043,1909,219,564,1706,536,1331,2108,2079,1787,1626,185,2020,727,2453],[112,533,1658,910,1868,580,1493,2331,1211,1223,2255,1287,1984,942,827,1126,661,1023,1377,22,822,2217,583,1779,929,1481,1862,202,924,545,45,1164,1075,745,2456,1752,2177,1220,1414,414,169,1854,848,306,1047,1917,181,259,1684,2055],[1832,1777,475,763,381,2344,958,1721,1975,193,482,1525,767,253,1734,2432,613,1326,2219,1313,464,2084,2369,761,773,1763,2140,36,183,1332,1897,990,1367,116,434,2431,2263,2458,899,1989,1674,1945,1985,1398,357,2228,403,2003,2150,2449]])