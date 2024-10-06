[[__TOC__]]

## Network format

| Byte | Function |
|  -- | -- | 
| 0-2 | Magic, used to recognize our packets | 
| 3 | Message type |
| 4-6 | Sender | 
| 7-9 | Originator (if different from sender) |

### Message types

| Type | Meaning | 
| -- | -- |
| 1 | Normal message to named station | 
| 2 | Heartbeat to all stations |