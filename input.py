def subset_sum(arr, target):
  """
  Fungsi untuk menemukan semua subset dari array yang jumlahnya sama dengan target.

  Args:
    arr: Array bilangan bulat.
    target: Nilai target.

  Returns:
    Daftar semua subset yang jumlah elemennya sama dengan target.
  """

  result = []

  def backtrack(index, current_sum, subset):
    """
    Fungsi rekursif untuk melakukan backtracking.

    Args:
      index: Indeks elemen saat ini dalam array.
      current_sum: Jumlah elemen dalam subset saat ini.
      subset: Subset saat ini.
    """
    if current_sum == target:
      result.append(subset.copy())
      return

    if index == len(arr):
      return

    # Tidak memilih elemen saat ini.
    backtrack(index + 1, current_sum, subset)

    # Memilih elemen saat ini.
    subset.append(arr[index])
    backtrack(index + 1, current_sum + arr[index], subset)
    subset.pop()

  backtrack(0, 0, [])
  return result

# Contoh penggunaan:
arr = [2, 4, 6, 8]
target = 10

subsets = subset_sum(arr, target)

# Mencetak hasil:
print("Daftar semua subset yang jumlah elemennya sama dengan target:")
for subset in subsets:
  print(subset)