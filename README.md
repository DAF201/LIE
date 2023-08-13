# LIE
Labor Is Evil

First thing first, I cannot guarentee everything happens properly like result ready, priority working properly, and thread pauses/resume/termeintes immidiently. Every functions are suggestion based.

Just provide some features like pause, resume, terminate, timeout, priority and return value to thread

I want to keep everything separate still, so I may use 'task' separately if i just need a pausable/resumable and terminatable thread at some point in the future

# features

Dash_board: provide priority and management

Clock: provide timeout

Task: provide pause, resume, terminate, and return value to thread

# note
1. clock is not inheritance from task, it is more like task class with more features
2. clock can terminate paused task, task cannot, you need to resume the task before terminate it otherwise it will stucked there
3. everything is suggestioned based! ordering, timing, resulting are not guarenteed
