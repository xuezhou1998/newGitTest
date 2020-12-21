import java.lang.*;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
public class project_mapper extends Mapper<LongWritable, Text, Text, Text> {
    private static final int MISSING = 9999;
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] string_list=line.split(" ");
        String the_key=string_list[0];
        int out_link_size= string_list.length-2;
        String last_output_value=string_list[0];
        Double PR = Double.parseDouble(string_list[string_list.length-1]);
        for (int i=0;i<out_link_size ;i++ ) {
            String output_string = String.format("%s, %s", the_key, PR/out_link_size);
            context.write(new Text(string_list[i+1]), new Text(output_string));
            last_output_value+=" ";
            last_output_value+=string_list[i+1];
        }
        //output n number of letter in the format of "A C B ..."
        context.write(new Text(the_key), new Text(last_output_value));

    }
}