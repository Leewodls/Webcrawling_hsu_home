def save_to_file(file_name, infos):

  file = open(f"{file_name}.csv", "w")

  file.write("position, company, Location, URL\n")

  for info in infos:
    file.write(
      f"{info['num']},{info['writer']}, {info['view']},{info['day']},{info['title']}\n"
    )

  file.close()