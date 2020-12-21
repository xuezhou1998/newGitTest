import java.io.IOException;
import org.apache.hadoop.io.IntWritable; import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import javax.print.DocFlavor;

public class project_reducer extends Reducer<Text, Text, Text, Text> {
    @Override
    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        Double PR_sum=0.0;
        String out_links="";
        for (Text value : values){
            String line = value.toString();
            if (line.contains(",")==true) {
                String[] string_list=line.split(",");
                String sourceLink = string_list[0];
                String sourceValue= string_list[1].replace(" ","");
                Double sourceValue_Double = Double.parseDouble(sourceValue);
                PR_sum+=sourceValue_Double;
            }
            else {
                out_links=line;

            }



        }
        String final_sv = String.format("%.6f", PR_sum);
        String final_value= out_links+" "+final_sv;
        context.write(new Text(key), new Text(final_value));
    }
}
