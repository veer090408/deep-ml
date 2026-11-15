def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
  if not a or not a[0]:
    return -1
  if len(a[0]) != len(b):
    return -1
  hasil = []
  for row in a:
    total_baris = 0
    for i in range(len(b)):
      total_baris += row[i] * b[i]
    hasil.append(total_baris)
  return hasil