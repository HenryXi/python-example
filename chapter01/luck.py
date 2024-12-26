import os

def remove_file(file_path):
    try:
        # 删除文件
        os.remove(file_path)
        print("文件已成功删除")
    except OSError as e:
        print("删除文件时出错:", e)


def generate_sql(csv_path):
    file_name = os.path.basename(csv_path)
    event_id = file_name.replace(".csv","")
    remove_file(event_id+"_insert.sql")
    with open(csv_path, 'r') as file_r:
        lines = file_r.readlines()

    for line in lines:
        items = [s.strip() for s in line.split(",") if s.strip()]
        if(len(items)==2):
            new_line = "INSERT INTO `event_spec` (event_id,model,spec_key) VALUES ("+event_id+",'"+items[0].strip().replace("\ufeff","")+"','"+items[1].strip()+"');\n"
            with open('/Users/xixiaoyong/Downloads/'+event_id+'_insert.sql', 'a') as file_w:
                file_w.write(new_line)
        
        if(len(items)==3):
            new_line = "INSERT INTO `event_spec` (event_id,model,spec_key,spec_arg) VALUES ("+event_id+",'"+items[0].strip().replace("\ufeff","")+"','"+items[1].strip()+"','"+items[2].strip()+"');\n"
            with open('/Users/xixiaoyong/Downloads/'+event_id+'_insert.sql', 'a') as file_w:
                file_w.write(new_line)

    

def main():
    generate_sql("/Users/xixiaoyong/Downloads/somebody_in_home.csv")


if __name__ == "__main__":
    main()


