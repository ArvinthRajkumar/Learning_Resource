def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area = lambda r: (r[2] - r[0]) * (r[3] - r[1])
    return inter / (area(a) + area(b) - inter)
def nms(boxes, scores, thr=0.5):
    order = sorted(range(len(boxes)), key=lambda i: -scores[i])
    keep = []
    while order:
        i = order.pop(0)
        keep.append(i)
        order = [j for j in order if iou(boxes[i], boxes[j]) < thr]
    return keep
boxes = [(10, 10, 50, 50), (12, 12, 52, 52), (100, 100, 140, 140), (11, 9, 49, 51)]
scores = [0.9, 0.8, 0.95, 0.7]
print("IoU of first two:", round(iou(boxes[0], boxes[1]), 3))
print("kept after NMS:", nms(boxes, scores))
