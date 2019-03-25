#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Coordinate mapping
mapping = {
0: np.array((0,1)),
1: np.array((0.0322581,1)),
2: np.array((0.0645161,1)),
3: np.array((0.0967742,1)),
4: np.array((0.129032,1)),
5: np.array((0.16129,1)),
6: np.array((0.193548,1)),
7: np.array((0.225806,1)),
8: np.array((0.258065,1)),
9: np.array((0.290323,1)),
10: np.array((0.322581,1)),
11: np.array((0.354839,1)),
12: np.array((0.387097,1)),
13: np.array((0.419355,1)),
14: np.array((0.451613,1)),
15: np.array((0.483871,1)),
16: np.array((0.516129,1)),
17: np.array((0.548387,1)),
18: np.array((0.580645,1)),
19: np.array((0.612903,1)),
20: np.array((0.645161,1)),
21: np.array((0.677419,1)),
22: np.array((0.709677,1)),
23: np.array((0.741935,1)),
24: np.array((0.774194,1)),
25: np.array((0.806452,1)),
26: np.array((0.83871,1)),
27: np.array((0.870968,1)),
28: np.array((0.903226,1)),
29: np.array((0.935484,1)),
30: np.array((0.967742,1)),
31: np.array((0,0.967742)),
32: np.array((0.0322581,0.967742)),
33: np.array((0.0645161,0.967742)),
34: np.array((0.0967742,0.967742)),
35: np.array((0.129032,0.967742)),
36: np.array((0.16129,0.967742)),
37: np.array((0.193548,0.967742)),
38: np.array((0.225806,0.967742)),
39: np.array((0.258065,0.967742)),
40: np.array((0.290323,0.967742)),
41: np.array((0.322581,0.967742)),
42: np.array((0.354839,0.967742)),
43: np.array((0.387097,0.967742)),
44: np.array((0.419355,0.967742)),
45: np.array((0.451613,0.967742)),
46: np.array((0.483871,0.967742)),
47: np.array((0.516129,0.967742)),
48: np.array((0.548387,0.967742)),
49: np.array((0.580645,0.967742)),
50: np.array((0.612903,0.967742)),
51: np.array((0.645161,0.967742)),
52: np.array((0.677419,0.967742)),
53: np.array((0.709677,0.967742)),
54: np.array((0.741935,0.967742)),
55: np.array((0.774194,0.967742)),
56: np.array((0.806452,0.967742)),
57: np.array((0.83871,0.967742)),
58: np.array((0.870968,0.967742)),
59: np.array((0.903226,0.967742)),
60: np.array((0.935484,0.967742)),
61: np.array((0.967742,0.967742)),
62: np.array((0,0.935484)),
63: np.array((0.0322581,0.935484)),
64: np.array((0.0645161,0.935484)),
65: np.array((0.0967742,0.935484)),
66: np.array((0.129032,0.935484)),
67: np.array((0.16129,0.935484)),
68: np.array((0.193548,0.935484)),
69: np.array((0.225806,0.935484)),
70: np.array((0.258065,0.935484)),
71: np.array((0.290323,0.935484)),
72: np.array((0.322581,0.935484)),
73: np.array((0.354839,0.935484)),
74: np.array((0.387097,0.935484)),
75: np.array((0.419355,0.935484)),
76: np.array((0.451613,0.935484)),
77: np.array((0.483871,0.935484)),
78: np.array((0.516129,0.935484)),
79: np.array((0.548387,0.935484)),
80: np.array((0.580645,0.935484)),
81: np.array((0.612903,0.935484)),
82: np.array((0.645161,0.935484)),
83: np.array((0.677419,0.935484)),
84: np.array((0.709677,0.935484)),
85: np.array((0.741935,0.935484)),
86: np.array((0.774194,0.935484)),
87: np.array((0.806452,0.935484)),
88: np.array((0.83871,0.935484)),
89: np.array((0.870968,0.935484)),
90: np.array((0.903226,0.935484)),
91: np.array((0.935484,0.935484)),
92: np.array((0.967742,0.935484)),
93: np.array((0,0.903226)),
94: np.array((0.0322581,0.903226)),
95: np.array((0.0645161,0.903226)),
96: np.array((0.0967742,0.903226)),
97: np.array((0.129032,0.903226)),
98: np.array((0.16129,0.903226)),
99: np.array((0.193548,0.903226)),
100: np.array((0.225806,0.903226)),
101: np.array((0.258065,0.903226)),
102: np.array((0.290323,0.903226)),
103: np.array((0.322581,0.903226)),
104: np.array((0.354839,0.903226)),
105: np.array((0.387097,0.903226)),
106: np.array((0.419355,0.903226)),
107: np.array((0.451613,0.903226)),
108: np.array((0.483871,0.903226)),
109: np.array((0.516129,0.903226)),
110: np.array((0.548387,0.903226)),
111: np.array((0.580645,0.903226)),
112: np.array((0.612903,0.903226)),
113: np.array((0.645161,0.903226)),
114: np.array((0.677419,0.903226)),
115: np.array((0.709677,0.903226)),
116: np.array((0.741935,0.903226)),
117: np.array((0.774194,0.903226)),
118: np.array((0.806452,0.903226)),
119: np.array((0.83871,0.903226)),
120: np.array((0.870968,0.903226)),
121: np.array((0.903226,0.903226)),
122: np.array((0.935484,0.903226)),
123: np.array((0.967742,0.903226)),
124: np.array((0,0.870968)),
125: np.array((0.0322581,0.870968)),
126: np.array((0.0645161,0.870968)),
127: np.array((0.0967742,0.870968)),
128: np.array((0.129032,0.870968)),
129: np.array((0.16129,0.870968)),
130: np.array((0.193548,0.870968)),
131: np.array((0.225806,0.870968)),
132: np.array((0.258065,0.870968)),
133: np.array((0.290323,0.870968)),
134: np.array((0.322581,0.870968)),
135: np.array((0.354839,0.870968)),
136: np.array((0.387097,0.870968)),
137: np.array((0.419355,0.870968)),
138: np.array((0.451613,0.870968)),
139: np.array((0.483871,0.870968)),
140: np.array((0.516129,0.870968)),
141: np.array((0.548387,0.870968)),
142: np.array((0.580645,0.870968)),
143: np.array((0.612903,0.870968)),
144: np.array((0.645161,0.870968)),
145: np.array((0.677419,0.870968)),
146: np.array((0.709677,0.870968)),
147: np.array((0.741935,0.870968)),
148: np.array((0.774194,0.870968)),
149: np.array((0.806452,0.870968)),
150: np.array((0.83871,0.870968)),
151: np.array((0.870968,0.870968)),
152: np.array((0.903226,0.870968)),
153: np.array((0.935484,0.870968)),
154: np.array((0.967742,0.870968)),
155: np.array((0,0.83871)),
156: np.array((0.0322581,0.83871)),
157: np.array((0.0645161,0.83871)),
158: np.array((0.0967742,0.83871)),
159: np.array((0.129032,0.83871)),
160: np.array((0.16129,0.83871)),
161: np.array((0.193548,0.83871)),
162: np.array((0.225806,0.83871)),
163: np.array((0.258065,0.83871)),
164: np.array((0.290323,0.83871)),
165: np.array((0.322581,0.83871)),
166: np.array((0.354839,0.83871)),
167: np.array((0.387097,0.83871)),
168: np.array((0.419355,0.83871)),
169: np.array((0.451613,0.83871)),
170: np.array((0.483871,0.83871)),
171: np.array((0.516129,0.83871)),
172: np.array((0.548387,0.83871)),
173: np.array((0.580645,0.83871)),
174: np.array((0.612903,0.83871)),
175: np.array((0.645161,0.83871)),
176: np.array((0.677419,0.83871)),
177: np.array((0.709677,0.83871)),
178: np.array((0.741935,0.83871)),
179: np.array((0.774194,0.83871)),
180: np.array((0.806452,0.83871)),
181: np.array((0.83871,0.83871)),
182: np.array((0.870968,0.83871)),
183: np.array((0.903226,0.83871)),
184: np.array((0.935484,0.83871)),
185: np.array((0.967742,0.83871)),
186: np.array((0,0.806452)),
187: np.array((0.0322581,0.806452)),
188: np.array((0.0645161,0.806452)),
189: np.array((0.0967742,0.806452)),
190: np.array((0.129032,0.806452)),
191: np.array((0.16129,0.806452)),
192: np.array((0.193548,0.806452)),
193: np.array((0.225806,0.806452)),
194: np.array((0.258065,0.806452)),
195: np.array((0.290323,0.806452)),
196: np.array((0.322581,0.806452)),
197: np.array((0.354839,0.806452)),
198: np.array((0.387097,0.806452)),
199: np.array((0.419355,0.806452)),
200: np.array((0.451613,0.806452)),
201: np.array((0.483871,0.806452)),
202: np.array((0.516129,0.806452)),
203: np.array((0.548387,0.806452)),
204: np.array((0.580645,0.806452)),
205: np.array((0.612903,0.806452)),
206: np.array((0.645161,0.806452)),
207: np.array((0.677419,0.806452)),
208: np.array((0.709677,0.806452)),
209: np.array((0.741935,0.806452)),
210: np.array((0.774194,0.806452)),
211: np.array((0.806452,0.806452)),
212: np.array((0.83871,0.806452)),
213: np.array((0.870968,0.806452)),
214: np.array((0.903226,0.806452)),
215: np.array((0.935484,0.806452)),
216: np.array((0.967742,0.806452)),
217: np.array((0,0.774194)),
218: np.array((0.0322581,0.774194)),
219: np.array((0.0645161,0.774194)),
220: np.array((0.0967742,0.774194)),
221: np.array((0.129032,0.774194)),
222: np.array((0.16129,0.774194)),
223: np.array((0.193548,0.774194)),
224: np.array((0.225806,0.774194)),
225: np.array((0.258065,0.774194)),
226: np.array((0.290323,0.774194)),
227: np.array((0.322581,0.774194)),
228: np.array((0.354839,0.774194)),
229: np.array((0.387097,0.774194)),
230: np.array((0.419355,0.774194)),
231: np.array((0.451613,0.774194)),
232: np.array((0.483871,0.774194)),
233: np.array((0.516129,0.774194)),
234: np.array((0.548387,0.774194)),
235: np.array((0.580645,0.774194)),
236: np.array((0.612903,0.774194)),
237: np.array((0.645161,0.774194)),
238: np.array((0.677419,0.774194)),
239: np.array((0.709677,0.774194)),
240: np.array((0.741935,0.774194)),
241: np.array((0.774194,0.774194)),
242: np.array((0.806452,0.774194)),
243: np.array((0.83871,0.774194)),
244: np.array((0.870968,0.774194)),
245: np.array((0.903226,0.774194)),
246: np.array((0.935484,0.774194)),
247: np.array((0.967742,0.774194)),
248: np.array((0,0.741935)),
249: np.array((0.0322581,0.741935)),
250: np.array((0.0645161,0.741935)),
251: np.array((0.0967742,0.741935)),
252: np.array((0.129032,0.741935)),
253: np.array((0.16129,0.741935)),
254: np.array((0.193548,0.741935)),
255: np.array((0.225806,0.741935)),
256: np.array((0.258065,0.741935)),
257: np.array((0.290323,0.741935)),
258: np.array((0.322581,0.741935)),
259: np.array((0.354839,0.741935)),
260: np.array((0.387097,0.741935)),
261: np.array((0.419355,0.741935)),
262: np.array((0.451613,0.741935)),
263: np.array((0.483871,0.741935)),
264: np.array((0.516129,0.741935)),
265: np.array((0.548387,0.741935)),
266: np.array((0.580645,0.741935)),
267: np.array((0.612903,0.741935)),
268: np.array((0.645161,0.741935)),
269: np.array((0.677419,0.741935)),
270: np.array((0.709677,0.741935)),
271: np.array((0.741935,0.741935)),
272: np.array((0.774194,0.741935)),
273: np.array((0.806452,0.741935)),
274: np.array((0.83871,0.741935)),
275: np.array((0.870968,0.741935)),
276: np.array((0.903226,0.741935)),
277: np.array((0.935484,0.741935)),
278: np.array((0.967742,0.741935)),
279: np.array((0,0.709677)),
280: np.array((0.0322581,0.709677)),
281: np.array((0.0645161,0.709677)),
282: np.array((0.0967742,0.709677)),
283: np.array((0.129032,0.709677)),
284: np.array((0.16129,0.709677)),
285: np.array((0.193548,0.709677)),
286: np.array((0.225806,0.709677)),
287: np.array((0.258065,0.709677)),
288: np.array((0.290323,0.709677)),
289: np.array((0.322581,0.709677)),
290: np.array((0.354839,0.709677)),
291: np.array((0.387097,0.709677)),
292: np.array((0.419355,0.709677)),
293: np.array((0.451613,0.709677)),
294: np.array((0.483871,0.709677)),
295: np.array((0.516129,0.709677)),
296: np.array((0.548387,0.709677)),
297: np.array((0.580645,0.709677)),
298: np.array((0.612903,0.709677)),
299: np.array((0.645161,0.709677)),
300: np.array((0.677419,0.709677)),
301: np.array((0.709677,0.709677)),
302: np.array((0.741935,0.709677)),
303: np.array((0.774194,0.709677)),
304: np.array((0.806452,0.709677)),
305: np.array((0.83871,0.709677)),
306: np.array((0.870968,0.709677)),
307: np.array((0.903226,0.709677)),
308: np.array((0.935484,0.709677)),
309: np.array((0.967742,0.709677)),
310: np.array((0,0.677419)),
311: np.array((0.0322581,0.677419)),
312: np.array((0.0645161,0.677419)),
313: np.array((0.0967742,0.677419)),
314: np.array((0.129032,0.677419)),
315: np.array((0.16129,0.677419)),
316: np.array((0.193548,0.677419)),
317: np.array((0.225806,0.677419)),
318: np.array((0.258065,0.677419)),
319: np.array((0.290323,0.677419)),
320: np.array((0.322581,0.677419)),
321: np.array((0.354839,0.677419)),
322: np.array((0.387097,0.677419)),
323: np.array((0.419355,0.677419)),
324: np.array((0.451613,0.677419)),
325: np.array((0.483871,0.677419)),
326: np.array((0.516129,0.677419)),
327: np.array((0.548387,0.677419)),
328: np.array((0.580645,0.677419)),
329: np.array((0.612903,0.677419)),
330: np.array((0.645161,0.677419)),
331: np.array((0.677419,0.677419)),
332: np.array((0.709677,0.677419)),
333: np.array((0.741935,0.677419)),
334: np.array((0.774194,0.677419)),
335: np.array((0.806452,0.677419)),
336: np.array((0.83871,0.677419)),
337: np.array((0.870968,0.677419)),
338: np.array((0.903226,0.677419)),
339: np.array((0.935484,0.677419)),
340: np.array((0.967742,0.677419)),
341: np.array((0,0.645161)),
342: np.array((0.0322581,0.645161)),
343: np.array((0.0645161,0.645161)),
344: np.array((0.0967742,0.645161)),
345: np.array((0.129032,0.645161)),
346: np.array((0.16129,0.645161)),
347: np.array((0.193548,0.645161)),
348: np.array((0.225806,0.645161)),
349: np.array((0.258065,0.645161)),
350: np.array((0.290323,0.645161)),
351: np.array((0.322581,0.645161)),
352: np.array((0.354839,0.645161)),
353: np.array((0.387097,0.645161)),
354: np.array((0.419355,0.645161)),
355: np.array((0.451613,0.645161)),
356: np.array((0.483871,0.645161)),
357: np.array((0.516129,0.645161)),
358: np.array((0.548387,0.645161)),
359: np.array((0.580645,0.645161)),
360: np.array((0.612903,0.645161)),
361: np.array((0.645161,0.645161)),
362: np.array((0.677419,0.645161)),
363: np.array((0.709677,0.645161)),
364: np.array((0.741935,0.645161)),
365: np.array((0.774194,0.645161)),
366: np.array((0.806452,0.645161)),
367: np.array((0.83871,0.645161)),
368: np.array((0.870968,0.645161)),
369: np.array((0.903226,0.645161)),
370: np.array((0.935484,0.645161)),
371: np.array((0.967742,0.645161)),
372: np.array((0,0.612903)),
373: np.array((0.0322581,0.612903)),
374: np.array((0.0645161,0.612903)),
375: np.array((0.0967742,0.612903)),
376: np.array((0.129032,0.612903)),
377: np.array((0.16129,0.612903)),
378: np.array((0.193548,0.612903)),
379: np.array((0.225806,0.612903)),
380: np.array((0.258065,0.612903)),
381: np.array((0.290323,0.612903)),
382: np.array((0.322581,0.612903)),
383: np.array((0.354839,0.612903)),
384: np.array((0.387097,0.612903)),
385: np.array((0.419355,0.612903)),
386: np.array((0.451613,0.612903)),
387: np.array((0.483871,0.612903)),
388: np.array((0.516129,0.612903)),
389: np.array((0.548387,0.612903)),
390: np.array((0.580645,0.612903)),
391: np.array((0.612903,0.612903)),
392: np.array((0.645161,0.612903)),
393: np.array((0.677419,0.612903)),
394: np.array((0.709677,0.612903)),
395: np.array((0.741935,0.612903)),
396: np.array((0.774194,0.612903)),
397: np.array((0.806452,0.612903)),
398: np.array((0.83871,0.612903)),
399: np.array((0.870968,0.612903)),
400: np.array((0.903226,0.612903)),
401: np.array((0.935484,0.612903)),
402: np.array((0.967742,0.612903)),
403: np.array((0,0.580645)),
404: np.array((0.0322581,0.580645)),
405: np.array((0.0645161,0.580645)),
406: np.array((0.0967742,0.580645)),
407: np.array((0.129032,0.580645)),
408: np.array((0.16129,0.580645)),
409: np.array((0.193548,0.580645)),
410: np.array((0.225806,0.580645)),
411: np.array((0.258065,0.580645)),
412: np.array((0.290323,0.580645)),
413: np.array((0.322581,0.580645)),
414: np.array((0.354839,0.580645)),
415: np.array((0.387097,0.580645)),
416: np.array((0.419355,0.580645)),
417: np.array((0.451613,0.580645)),
418: np.array((0.483871,0.580645)),
419: np.array((0.516129,0.580645)),
420: np.array((0.548387,0.580645)),
421: np.array((0.580645,0.580645)),
422: np.array((0.612903,0.580645)),
423: np.array((0.645161,0.580645)),
424: np.array((0.677419,0.580645)),
425: np.array((0.709677,0.580645)),
426: np.array((0.741935,0.580645)),
427: np.array((0.774194,0.580645)),
428: np.array((0.806452,0.580645)),
429: np.array((0.83871,0.580645)),
430: np.array((0.870968,0.580645)),
431: np.array((0.903226,0.580645)),
432: np.array((0.935484,0.580645)),
433: np.array((0.967742,0.580645)),
434: np.array((0,0.548387)),
435: np.array((0.0322581,0.548387)),
436: np.array((0.0645161,0.548387)),
437: np.array((0.0967742,0.548387)),
438: np.array((0.129032,0.548387)),
439: np.array((0.16129,0.548387)),
440: np.array((0.193548,0.548387)),
441: np.array((0.225806,0.548387)),
442: np.array((0.258065,0.548387)),
443: np.array((0.290323,0.548387)),
444: np.array((0.322581,0.548387)),
445: np.array((0.354839,0.548387)),
446: np.array((0.387097,0.548387)),
447: np.array((0.419355,0.548387)),
448: np.array((0.451613,0.548387)),
449: np.array((0.483871,0.548387)),
450: np.array((0.516129,0.548387)),
451: np.array((0.548387,0.548387)),
452: np.array((0.580645,0.548387)),
453: np.array((0.612903,0.548387)),
454: np.array((0.645161,0.548387)),
455: np.array((0.677419,0.548387)),
456: np.array((0.709677,0.548387)),
457: np.array((0.741935,0.548387)),
458: np.array((0.774194,0.548387)),
459: np.array((0.806452,0.548387)),
460: np.array((0.83871,0.548387)),
461: np.array((0.870968,0.548387)),
462: np.array((0.903226,0.548387)),
463: np.array((0.935484,0.548387)),
464: np.array((0.967742,0.548387)),
465: np.array((0,0.516129)),
466: np.array((0.0322581,0.516129)),
467: np.array((0.0645161,0.516129)),
468: np.array((0.0967742,0.516129)),
469: np.array((0.129032,0.516129)),
470: np.array((0.16129,0.516129)),
471: np.array((0.193548,0.516129)),
472: np.array((0.225806,0.516129)),
473: np.array((0.258065,0.516129)),
474: np.array((0.290323,0.516129)),
475: np.array((0.322581,0.516129)),
476: np.array((0.354839,0.516129)),
477: np.array((0.387097,0.516129)),
478: np.array((0.419355,0.516129)),
479: np.array((0.451613,0.516129)),
480: np.array((0.483871,0.516129)),
481: np.array((0.516129,0.516129)),
482: np.array((0.548387,0.516129)),
483: np.array((0.580645,0.516129)),
484: np.array((0.612903,0.516129)),
485: np.array((0.645161,0.516129)),
486: np.array((0.677419,0.516129)),
487: np.array((0.709677,0.516129)),
488: np.array((0.741935,0.516129)),
489: np.array((0.774194,0.516129)),
490: np.array((0.806452,0.516129)),
491: np.array((0.83871,0.516129)),
492: np.array((0.870968,0.516129)),
493: np.array((0.903226,0.516129)),
494: np.array((0.935484,0.516129)),
495: np.array((0.967742,0.516129)),
496: np.array((0,0.483871)),
497: np.array((0.0322581,0.483871)),
498: np.array((0.0645161,0.483871)),
499: np.array((0.0967742,0.483871)),
500: np.array((0.129032,0.483871)),
501: np.array((0.16129,0.483871)),
502: np.array((0.193548,0.483871)),
503: np.array((0.225806,0.483871)),
504: np.array((0.258065,0.483871)),
505: np.array((0.290323,0.483871)),
506: np.array((0.322581,0.483871)),
507: np.array((0.354839,0.483871)),
508: np.array((0.387097,0.483871)),
509: np.array((0.419355,0.483871)),
510: np.array((0.451613,0.483871)),
511: np.array((0.483871,0.483871)),
512: np.array((0.516129,0.483871)),
513: np.array((0.548387,0.483871)),
514: np.array((0.580645,0.483871)),
515: np.array((0.612903,0.483871)),
516: np.array((0.645161,0.483871)),
517: np.array((0.677419,0.483871)),
518: np.array((0.709677,0.483871)),
519: np.array((0.741935,0.483871)),
520: np.array((0.774194,0.483871)),
521: np.array((0.806452,0.483871)),
522: np.array((0.83871,0.483871)),
523: np.array((0.870968,0.483871)),
524: np.array((0.903226,0.483871)),
525: np.array((0.935484,0.483871)),
526: np.array((0.967742,0.483871)),
527: np.array((0,0.451613)),
528: np.array((0.0322581,0.451613)),
529: np.array((0.0645161,0.451613)),
530: np.array((0.0967742,0.451613)),
531: np.array((0.129032,0.451613)),
532: np.array((0.16129,0.451613)),
533: np.array((0.193548,0.451613)),
534: np.array((0.225806,0.451613)),
535: np.array((0.258065,0.451613)),
536: np.array((0.290323,0.451613)),
537: np.array((0.322581,0.451613)),
538: np.array((0.354839,0.451613)),
539: np.array((0.387097,0.451613)),
540: np.array((0.419355,0.451613)),
541: np.array((0.451613,0.451613)),
542: np.array((0.483871,0.451613)),
543: np.array((0.516129,0.451613)),
544: np.array((0.548387,0.451613)),
545: np.array((0.580645,0.451613)),
546: np.array((0.612903,0.451613)),
547: np.array((0.645161,0.451613)),
548: np.array((0.677419,0.451613)),
549: np.array((0.709677,0.451613)),
550: np.array((0.741935,0.451613)),
551: np.array((0.774194,0.451613)),
552: np.array((0.806452,0.451613)),
553: np.array((0.83871,0.451613)),
554: np.array((0.870968,0.451613)),
555: np.array((0.903226,0.451613)),
556: np.array((0.935484,0.451613)),
557: np.array((0.967742,0.451613)),
558: np.array((0,0.419355)),
559: np.array((0.0322581,0.419355)),
560: np.array((0.0645161,0.419355)),
561: np.array((0.0967742,0.419355)),
562: np.array((0.129032,0.419355)),
563: np.array((0.16129,0.419355)),
564: np.array((0.193548,0.419355)),
565: np.array((0.225806,0.419355)),
566: np.array((0.258065,0.419355)),
567: np.array((0.290323,0.419355)),
568: np.array((0.322581,0.419355)),
569: np.array((0.354839,0.419355)),
570: np.array((0.387097,0.419355)),
571: np.array((0.419355,0.419355)),
572: np.array((0.451613,0.419355)),
573: np.array((0.483871,0.419355)),
574: np.array((0.516129,0.419355)),
575: np.array((0.548387,0.419355)),
576: np.array((0.580645,0.419355)),
577: np.array((0.612903,0.419355)),
578: np.array((0.645161,0.419355)),
579: np.array((0.677419,0.419355)),
580: np.array((0.709677,0.419355)),
581: np.array((0.741935,0.419355)),
582: np.array((0.774194,0.419355)),
583: np.array((0.806452,0.419355)),
584: np.array((0.83871,0.419355)),
585: np.array((0.870968,0.419355)),
586: np.array((0.903226,0.419355)),
587: np.array((0.935484,0.419355)),
588: np.array((0.967742,0.419355)),
589: np.array((0,0.387097)),
590: np.array((0.0322581,0.387097)),
591: np.array((0.0645161,0.387097)),
592: np.array((0.0967742,0.387097)),
593: np.array((0.129032,0.387097)),
594: np.array((0.16129,0.387097)),
595: np.array((0.193548,0.387097)),
596: np.array((0.225806,0.387097)),
597: np.array((0.258065,0.387097)),
598: np.array((0.290323,0.387097)),
599: np.array((0.322581,0.387097)),
600: np.array((0.354839,0.387097)),
601: np.array((0.387097,0.387097)),
602: np.array((0.419355,0.387097)),
603: np.array((0.451613,0.387097)),
604: np.array((0.483871,0.387097)),
605: np.array((0.516129,0.387097)),
606: np.array((0.548387,0.387097)),
607: np.array((0.580645,0.387097)),
608: np.array((0.612903,0.387097)),
609: np.array((0.645161,0.387097)),
610: np.array((0.677419,0.387097)),
611: np.array((0.709677,0.387097)),
612: np.array((0.741935,0.387097)),
613: np.array((0.774194,0.387097)),
614: np.array((0.806452,0.387097)),
615: np.array((0.83871,0.387097)),
616: np.array((0.870968,0.387097)),
617: np.array((0.903226,0.387097)),
618: np.array((0.935484,0.387097)),
619: np.array((0.967742,0.387097)),
620: np.array((0,0.354839)),
621: np.array((0.0322581,0.354839)),
622: np.array((0.0645161,0.354839)),
623: np.array((0.0967742,0.354839)),
624: np.array((0.129032,0.354839)),
625: np.array((0.16129,0.354839)),
626: np.array((0.193548,0.354839)),
627: np.array((0.225806,0.354839)),
628: np.array((0.258065,0.354839)),
629: np.array((0.290323,0.354839)),
630: np.array((0.322581,0.354839)),
631: np.array((0.354839,0.354839)),
632: np.array((0.387097,0.354839)),
633: np.array((0.419355,0.354839)),
634: np.array((0.451613,0.354839)),
635: np.array((0.483871,0.354839)),
636: np.array((0.516129,0.354839)),
637: np.array((0.548387,0.354839)),
638: np.array((0.580645,0.354839)),
639: np.array((0.612903,0.354839)),
640: np.array((0.645161,0.354839)),
641: np.array((0.677419,0.354839)),
642: np.array((0.709677,0.354839)),
643: np.array((0.741935,0.354839)),
644: np.array((0.774194,0.354839)),
645: np.array((0.806452,0.354839)),
646: np.array((0.83871,0.354839)),
647: np.array((0.870968,0.354839)),
648: np.array((0.903226,0.354839)),
649: np.array((0.935484,0.354839)),
650: np.array((0.967742,0.354839)),
651: np.array((0,0.322581)),
652: np.array((0.0322581,0.322581)),
653: np.array((0.0645161,0.322581)),
654: np.array((0.0967742,0.322581)),
655: np.array((0.129032,0.322581)),
656: np.array((0.16129,0.322581)),
657: np.array((0.193548,0.322581)),
658: np.array((0.225806,0.322581)),
659: np.array((0.258065,0.322581)),
660: np.array((0.290323,0.322581)),
661: np.array((0.322581,0.322581)),
662: np.array((0.354839,0.322581)),
663: np.array((0.387097,0.322581)),
664: np.array((0.419355,0.322581)),
665: np.array((0.451613,0.322581)),
666: np.array((0.483871,0.322581)),
667: np.array((0.516129,0.322581)),
668: np.array((0.548387,0.322581)),
669: np.array((0.580645,0.322581)),
670: np.array((0.612903,0.322581)),
671: np.array((0.645161,0.322581)),
672: np.array((0.677419,0.322581)),
673: np.array((0.709677,0.322581)),
674: np.array((0.741935,0.322581)),
675: np.array((0.774194,0.322581)),
676: np.array((0.806452,0.322581)),
677: np.array((0.83871,0.322581)),
678: np.array((0.870968,0.322581)),
679: np.array((0.903226,0.322581)),
680: np.array((0.935484,0.322581)),
681: np.array((0.967742,0.322581)),
682: np.array((0,0.290323)),
683: np.array((0.0322581,0.290323)),
684: np.array((0.0645161,0.290323)),
685: np.array((0.0967742,0.290323)),
686: np.array((0.129032,0.290323)),
687: np.array((0.16129,0.290323)),
688: np.array((0.193548,0.290323)),
689: np.array((0.225806,0.290323)),
690: np.array((0.258065,0.290323)),
691: np.array((0.290323,0.290323)),
692: np.array((0.322581,0.290323)),
693: np.array((0.354839,0.290323)),
694: np.array((0.387097,0.290323)),
695: np.array((0.419355,0.290323)),
696: np.array((0.451613,0.290323)),
697: np.array((0.483871,0.290323)),
698: np.array((0.516129,0.290323)),
699: np.array((0.548387,0.290323)),
700: np.array((0.580645,0.290323)),
701: np.array((0.612903,0.290323)),
702: np.array((0.645161,0.290323)),
703: np.array((0.677419,0.290323)),
704: np.array((0.709677,0.290323)),
705: np.array((0.741935,0.290323)),
706: np.array((0.774194,0.290323)),
707: np.array((0.806452,0.290323)),
708: np.array((0.83871,0.290323)),
709: np.array((0.870968,0.290323)),
710: np.array((0.903226,0.290323)),
711: np.array((0.935484,0.290323)),
712: np.array((0.967742,0.290323)),
713: np.array((0,0.258065)),
714: np.array((0.0322581,0.258065)),
715: np.array((0.0645161,0.258065)),
716: np.array((0.0967742,0.258065)),
717: np.array((0.129032,0.258065)),
718: np.array((0.16129,0.258065)),
719: np.array((0.193548,0.258065)),
720: np.array((0.225806,0.258065)),
721: np.array((0.258065,0.258065)),
722: np.array((0.290323,0.258065)),
723: np.array((0.322581,0.258065)),
724: np.array((0.354839,0.258065)),
725: np.array((0.387097,0.258065)),
726: np.array((0.419355,0.258065)),
727: np.array((0.451613,0.258065)),
728: np.array((0.483871,0.258065)),
729: np.array((0.516129,0.258065)),
730: np.array((0.548387,0.258065)),
731: np.array((0.580645,0.258065)),
732: np.array((0.612903,0.258065)),
733: np.array((0.645161,0.258065)),
734: np.array((0.677419,0.258065)),
735: np.array((0.709677,0.258065)),
736: np.array((0.741935,0.258065)),
737: np.array((0.774194,0.258065)),
738: np.array((0.806452,0.258065)),
739: np.array((0.83871,0.258065)),
740: np.array((0.870968,0.258065)),
741: np.array((0.903226,0.258065)),
742: np.array((0.935484,0.258065)),
743: np.array((0.967742,0.258065)),
744: np.array((0,0.225806)),
745: np.array((0.0322581,0.225806)),
746: np.array((0.0645161,0.225806)),
747: np.array((0.0967742,0.225806)),
748: np.array((0.129032,0.225806)),
749: np.array((0.16129,0.225806)),
750: np.array((0.193548,0.225806)),
751: np.array((0.225806,0.225806)),
752: np.array((0.258065,0.225806)),
753: np.array((0.290323,0.225806)),
754: np.array((0.322581,0.225806)),
755: np.array((0.354839,0.225806)),
756: np.array((0.387097,0.225806)),
757: np.array((0.419355,0.225806)),
758: np.array((0.451613,0.225806)),
759: np.array((0.483871,0.225806)),
760: np.array((0.516129,0.225806)),
761: np.array((0.548387,0.225806)),
762: np.array((0.580645,0.225806)),
763: np.array((0.612903,0.225806)),
764: np.array((0.645161,0.225806)),
765: np.array((0.677419,0.225806)),
766: np.array((0.709677,0.225806)),
767: np.array((0.741935,0.225806)),
768: np.array((0.774194,0.225806)),
769: np.array((0.806452,0.225806)),
770: np.array((0.83871,0.225806)),
771: np.array((0.870968,0.225806)),
772: np.array((0.903226,0.225806)),
773: np.array((0.935484,0.225806)),
774: np.array((0.967742,0.225806)),
775: np.array((0,0.193548)),
776: np.array((0.0322581,0.193548)),
777: np.array((0.0645161,0.193548)),
778: np.array((0.0967742,0.193548)),
779: np.array((0.129032,0.193548)),
780: np.array((0.16129,0.193548)),
781: np.array((0.193548,0.193548)),
782: np.array((0.225806,0.193548)),
783: np.array((0.258065,0.193548)),
784: np.array((0.290323,0.193548)),
785: np.array((0.322581,0.193548)),
786: np.array((0.354839,0.193548)),
787: np.array((0.387097,0.193548)),
788: np.array((0.419355,0.193548)),
789: np.array((0.451613,0.193548)),
790: np.array((0.483871,0.193548)),
791: np.array((0.516129,0.193548)),
792: np.array((0.548387,0.193548)),
793: np.array((0.580645,0.193548)),
794: np.array((0.612903,0.193548)),
795: np.array((0.645161,0.193548)),
796: np.array((0.677419,0.193548)),
797: np.array((0.709677,0.193548)),
798: np.array((0.741935,0.193548)),
799: np.array((0.774194,0.193548)),
800: np.array((0.806452,0.193548)),
801: np.array((0.83871,0.193548)),
802: np.array((0.870968,0.193548)),
803: np.array((0.903226,0.193548)),
804: np.array((0.935484,0.193548)),
805: np.array((0.967742,0.193548)),
806: np.array((0,0.16129)),
807: np.array((0.0322581,0.16129)),
808: np.array((0.0645161,0.16129)),
809: np.array((0.0967742,0.16129)),
810: np.array((0.129032,0.16129)),
811: np.array((0.16129,0.16129)),
812: np.array((0.193548,0.16129)),
813: np.array((0.225806,0.16129)),
814: np.array((0.258065,0.16129)),
815: np.array((0.290323,0.16129)),
816: np.array((0.322581,0.16129)),
817: np.array((0.354839,0.16129)),
818: np.array((0.387097,0.16129)),
819: np.array((0.419355,0.16129)),
820: np.array((0.451613,0.16129)),
821: np.array((0.483871,0.16129)),
822: np.array((0.516129,0.16129)),
823: np.array((0.548387,0.16129)),
824: np.array((0.580645,0.16129)),
825: np.array((0.612903,0.16129)),
826: np.array((0.645161,0.16129)),
827: np.array((0.677419,0.16129)),
828: np.array((0.709677,0.16129)),
829: np.array((0.741935,0.16129)),
830: np.array((0.774194,0.16129)),
831: np.array((0.806452,0.16129)),
832: np.array((0.83871,0.16129)),
833: np.array((0.870968,0.16129)),
834: np.array((0.903226,0.16129)),
835: np.array((0.935484,0.16129)),
836: np.array((0.967742,0.16129)),
837: np.array((0,0.129032)),
838: np.array((0.0322581,0.129032)),
839: np.array((0.0645161,0.129032)),
840: np.array((0.0967742,0.129032)),
841: np.array((0.129032,0.129032)),
842: np.array((0.16129,0.129032)),
843: np.array((0.193548,0.129032)),
844: np.array((0.225806,0.129032)),
845: np.array((0.258065,0.129032)),
846: np.array((0.290323,0.129032)),
847: np.array((0.322581,0.129032)),
848: np.array((0.354839,0.129032)),
849: np.array((0.387097,0.129032)),
850: np.array((0.419355,0.129032)),
851: np.array((0.451613,0.129032)),
852: np.array((0.483871,0.129032)),
853: np.array((0.516129,0.129032)),
854: np.array((0.548387,0.129032)),
855: np.array((0.580645,0.129032)),
856: np.array((0.612903,0.129032)),
857: np.array((0.645161,0.129032)),
858: np.array((0.677419,0.129032)),
859: np.array((0.709677,0.129032)),
860: np.array((0.741935,0.129032)),
861: np.array((0.774194,0.129032)),
862: np.array((0.806452,0.129032)),
863: np.array((0.83871,0.129032)),
864: np.array((0.870968,0.129032)),
865: np.array((0.903226,0.129032)),
866: np.array((0.935484,0.129032)),
867: np.array((0.967742,0.129032)),
868: np.array((0,0.0967742)),
869: np.array((0.0322581,0.0967742)),
870: np.array((0.0645161,0.0967742)),
871: np.array((0.0967742,0.0967742)),
872: np.array((0.129032,0.0967742)),
873: np.array((0.16129,0.0967742)),
874: np.array((0.193548,0.0967742)),
875: np.array((0.225806,0.0967742)),
876: np.array((0.258065,0.0967742)),
877: np.array((0.290323,0.0967742)),
878: np.array((0.322581,0.0967742)),
879: np.array((0.354839,0.0967742)),
880: np.array((0.387097,0.0967742)),
881: np.array((0.419355,0.0967742)),
882: np.array((0.451613,0.0967742)),
883: np.array((0.483871,0.0967742)),
884: np.array((0.516129,0.0967742)),
885: np.array((0.548387,0.0967742)),
886: np.array((0.580645,0.0967742)),
887: np.array((0.612903,0.0967742)),
888: np.array((0.645161,0.0967742)),
889: np.array((0.677419,0.0967742)),
890: np.array((0.709677,0.0967742)),
891: np.array((0.741935,0.0967742)),
892: np.array((0.774194,0.0967742)),
893: np.array((0.806452,0.0967742)),
894: np.array((0.83871,0.0967742)),
895: np.array((0.870968,0.0967742)),
896: np.array((0.903226,0.0967742)),
897: np.array((0.935484,0.0967742)),
898: np.array((0.967742,0.0967742)),
899: np.array((0,0.0645161)),
900: np.array((0.0322581,0.0645161)),
901: np.array((0.0645161,0.0645161)),
902: np.array((0.0967742,0.0645161)),
903: np.array((0.129032,0.0645161)),
904: np.array((0.16129,0.0645161)),
905: np.array((0.193548,0.0645161)),
906: np.array((0.225806,0.0645161)),
907: np.array((0.258065,0.0645161)),
908: np.array((0.290323,0.0645161)),
909: np.array((0.322581,0.0645161)),
910: np.array((0.354839,0.0645161)),
911: np.array((0.387097,0.0645161)),
912: np.array((0.419355,0.0645161)),
913: np.array((0.451613,0.0645161)),
914: np.array((0.483871,0.0645161)),
915: np.array((0.516129,0.0645161)),
916: np.array((0.548387,0.0645161)),
917: np.array((0.580645,0.0645161)),
918: np.array((0.612903,0.0645161)),
919: np.array((0.645161,0.0645161)),
920: np.array((0.677419,0.0645161)),
921: np.array((0.709677,0.0645161)),
922: np.array((0.741935,0.0645161)),
923: np.array((0.774194,0.0645161)),
924: np.array((0.806452,0.0645161)),
925: np.array((0.83871,0.0645161)),
926: np.array((0.870968,0.0645161)),
927: np.array((0.903226,0.0645161)),
928: np.array((0.935484,0.0645161)),
929: np.array((0.967742,0.0645161)),
930: np.array((0,0.0322581)),
931: np.array((0.0322581,0.0322581)),
932: np.array((0.0645161,0.0322581)),
933: np.array((0.0967742,0.0322581)),
934: np.array((0.129032,0.0322581)),
935: np.array((0.16129,0.0322581)),
936: np.array((0.193548,0.0322581)),
937: np.array((0.225806,0.0322581)),
938: np.array((0.258065,0.0322581)),
939: np.array((0.290323,0.0322581)),
940: np.array((0.322581,0.0322581)),
941: np.array((0.354839,0.0322581)),
942: np.array((0.387097,0.0322581)),
943: np.array((0.419355,0.0322581)),
944: np.array((0.451613,0.0322581)),
945: np.array((0.483871,0.0322581)),
946: np.array((0.516129,0.0322581)),
947: np.array((0.548387,0.0322581)),
948: np.array((0.580645,0.0322581)),
949: np.array((0.612903,0.0322581)),
950: np.array((0.645161,0.0322581)),
951: np.array((0.677419,0.0322581)),
952: np.array((0.709677,0.0322581)),
953: np.array((0.741935,0.0322581)),
954: np.array((0.774194,0.0322581)),
955: np.array((0.806452,0.0322581)),
956: np.array((0.83871,0.0322581)),
957: np.array((0.870968,0.0322581)),
958: np.array((0.903226,0.0322581)),
959: np.array((0.935484,0.0322581)),
960: np.array((0.967742,0.0322581)),
}

G = nx.read_gml('network.gml')
G = nx.convert_node_labels_to_integers(G)

nx.draw(G, pos=mapping, with_labels=True, node_size=350, node_color='black', font_color='w', font_size=9)
plt.show()
