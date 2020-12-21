import java.text.Format;
import java.util.*;
//import java.util.Arrays.fill();
//Wxzcmpsc1998125!
public class Main {

    public static void main(String[] args) {
//        String line="2020-02-02,Suffolk,Massachusetts,25025,1,0";
//
//        String[] line_array=line.split(",");
//        //System.out.println(line_array[0]);
//        if (line_array[0].equals("2020-02-02")){
//            String state_string ="Alabama,ALxxxxxx" +
//                    "Alaska,AKxxxxxx" +
//                    "Arizona,AZxxxxxx" +
//                    "Arkansas,ARxxxxxx" +
//                    "California,CAxxxxxx" +
//                    "Colorado,COxxxxxx" +
//                    "Connecticut,CTxxxxxx" +
//                    "Delaware,DExxxxxx" +
//                    "District of Columbia,DCxxxxxx" +
//                    "Florida,FLxxxxxx" +
//                    "Georgia,GAxxxxxx" +
//                    "Hawaii,HIxxxxxx" +
//                    "Idaho,IDxxxxxx" +
//                    "Illinois,ILxxxxxx" +
//                    "Indiana,INxxxxxx" +
//                    "Iowa,IAxxxxxx" +
//                    "Kansas,KSxxxxxx" +
//                    "Kentucky,KYxxxxxx" +
//                    "Louisiana,LAxxxxxx" +
//                    "Maine,MExxxxxx" +
//                    "Maryland,MDxxxxxx" +
//                    "Massachusetts,MAxxxxxx" +
//                    "Michigan,MIxxxxxx" +
//                    "Minnesota,MNxxxxxx" +
//                    "Mississippi,MSxxxxxx" +
//                    "Missouri,MOxxxxxx" +
//                    "Montana,MTxxxxxx" +
//                    "Nebraska,NExxxxxx" +
//                    "Nevada,NVxxxxxx" +
//                    "New Hampshire,NHxxxxxx" +
//                    "New Jersey,NJxxxxxx" +
//                    "New Mexico,NMxxxxxx" +
//                    "New York,NYxxxxxx" +
//                    "North Carolina,NCxxxxxx" +
//                    "North Dakota,NDxxxxxx" +
//                    "Ohio,OHxxxxxx" +
//                    "Oklahoma,OKxxxxxx" +
//                    "Oregon,ORxxxxxx" +
//                    "Pennsylvania,PAxxxxxx" +
//                    "Rhode Island,RIxxxxxx" +
//                    "South Carolina,SCxxxxxx" +
//                    "South Dakota,SDxxxxxx" +
//                    "Tennessee,TNxxxxxx" +
//                    "Texas,TXxxxxxx" +
//                    "Utah,UTxxxxxx" +
//                    "Vermont,VTxxxxxx" +
//                    "Virginia,VAxxxxxx" +
//                    "Washington,WAxxxxxx" +
//                    "West Virginia,WVxxxxxx" +
//                    "Wisconsin,WIxxxxxx" +
//                    "Wyoming,WYxxxxxx";
//            String[] states_array= state_string.split("xxxxxx");
//            Dictionary<String,String> mydict= new Hashtable();
//
//            for (int i = 0; i<states_array.length;i++){
//                String[] subarray=states_array[i].split(",");
//                mydict.put(subarray[0],subarray[1]);
//                //System.out.print(subarray[1]);
//            }
//
//            //System.out.print(String.format("%s", states_array[5]))
//            String state_alpha= mydict.get(line_array[2].toString());
//
//            String final_string = String.join(",",line_array[0],line_array[1],state_alpha,line_array[3],
//                    line_array[4],line_array[5]);
//            //System.out.println(final_string);



        //Object textinput="2020-10-01,Kankakee,IL,17091,2816,77, 0";
//        Object textinput="1019,1229,1558,2072,2523,Miami-Dade,FL,2019";
//        int branch;
//        String county;
//        String state;
//        String year;
//        String final_value;
//        String final_key;
//        String[] text_arr=textinput.toString().split(",");
//        if (text_arr[0].split("-")[0].equals("2020")){
//            System.out.println(text_arr[0].split("-")[0].toString());
//             county = text_arr[1];
//             state= text_arr[2];
//             branch=0;
//             final_key=String.join(",", county,state);
//             final_value=String.join(",",text_arr[3],text_arr[4],text_arr[5]);
//    }
//        else {
//            county=text_arr[5];
//            state=text_arr[6];
//            year= text_arr[7];
//            branch=1;
//            final_key=String.join(",", county,state);
//            final_value=String.join(",",text_arr[0],text_arr[1],text_arr[2],text_arr[3],text_arr[4],year);
//
//        }
//
//        System.out.println(String.format("%s : %s", final_key,final_value));

//        String inputText="Wayne,IA:\t481,502,664,885,898,2019#519,543,715,889,970,2021#19185,89,3#465,489,650,856,885,2018#497,522,687,900,931,2020#";
//        String state_county=inputText.toString().split(":")[0];
//        String[] numArr = inputText.toString().split(":")[1].split("#");
//
//        if (numArr.length>=5){
//            int[][] doubleintarr={{1,2},{3,4},{5,6}};
//            int infection=0;
//            int death=0;
//            ArrayList<String[]> rents= new ArrayList<>();
//            for (int i = 0; i < numArr.length; i++) {
//                String[] currArr=numArr[i].split(",");
//                if (currArr.length==3){
//                    infection=Integer.valueOf(currArr[1]);
//                    death=Integer.valueOf(currArr[2]);
//                }
//                else if (currArr.length==6){
//                    for (int j = 0; j < currArr.length; j++) {
////                    System.out.print(currArr[j].toString()+"&");
//                    }
////                System.out.print("#");
//                    rents.add(currArr);
//
//                }
//
//            }
//            System.out.println(doubleintarr[2][1]);
//            Integer aaa=57777777;
//            System.out.println(aaa.toString());
//            double xs=5.5;
//            int aaaaaa=(int) xs;
//        }

        //System.out.println(predict(rents,infection,death));











        String input1="891,53,86,126,72,Walton,FL,2021";//length8
        String input2="89,953,186,526,192,Walton,FL,2019";//length8
        String input3="891,53,106,156,1792,Walton,FL,2020";//length8
        String input4="89,93,108,156,792,Walton,FL,2018";//length8
        String input5="Walton,FL,217,0,514,561,697,913,1071";//length9
        String inputx="Yancey,NC,217,0,514,561,697,913,1071";//length9
        String[] inputarrs={input1,input2,input3,input4,input5};
        String[] inputarr=input1.split(",");
        String county_state="";
        if (inputarr.length==8){
             county_state=String.join(",",inputarr[5],inputarr[6]);

        }
        else if (inputarr.length==9){
            county_state=String.join(",",inputarr[0],inputarr[1]);
        }

        reduce(county_state, inputarrs);

    }

    public static void reduce (String key, String value[]){
        String county_state= key;


        int[] var2020 =new int[5] ;
        Arrays.fill(var2020,0);
        int[] var2021=new int[5];
        Arrays.fill(var2021,0);
        int[] var2019=new int[5];
        Arrays.fill(var2019,0);
        int infection_num=0;


        for (int j = 0; j < value.length; j++) {
            //for loop wrapped
//            System.out.println(value[j]+"st");
            String[] inputarr=value[j].split(",");

            if (inputarr.length==8){
//            county_state=String.join(",",inputarr[5],inputarr[6]);
//                System.out.println("x2021");
//                System.out.println(inputarr[7]+"xxxxx");
                if (inputarr[7].equals("2021")){
//                    System.out.println("x2021");
                    for (int i = 0; i <5 ; i++) {
                        var2021[i]=Integer.valueOf(inputarr[i]);

                    }

                }
                else if (inputarr[7].equals("2020")){
                    for (int i = 0; i <5 ; i++) {
                        var2020[i]=Integer.valueOf(inputarr[i]);
                    }
                }
                else if (inputarr[7].equals("2019")){
                    for (int i = 0; i <5 ; i++) {
                        var2019[i]=Integer.valueOf(inputarr[i]);

                    }
                }

            }
            else if (inputarr.length==9){
//            county_state=String.join(",",inputarr[0],inputarr[1]);
                infection_num= Integer.valueOf(inputarr[2]);

            }//for loop wrapped end
        }

        int[] var2020_2021 =new int[5] ;
        Arrays.fill(var2020_2021,0);
        int[] var2019_2020 =new int[5] ;
        Arrays.fill(var2019_2020,0);
        int[] varSlope_Change =new int[5] ;
        Arrays.fill(varSlope_Change,0);
        int[] resultarr =new int[5] ;
        Arrays.fill(resultarr,0);

        for (int i = 0; i <5 ; i++) {
            var2019_2020[i]=var2020[i]-var2019[i];
            var2020_2021[i]=var2021[i]-var2020[i];
            varSlope_Change[i]=var2020_2021[i]-var2019_2020[i];
//            System.out.println(String.valueOf(var2019_2020[i])+String.valueOf(var2020_2021[i])
//            +String.valueOf(varSlope_Change[i]));
            if (varSlope_Change[i]*infection_num<0){
                resultarr[i]=-1;
            }
            else if (varSlope_Change[i]*infection_num>0){
                resultarr[i]=1;
            }
            else {
                resultarr[i]=0;
            }
            System.out.println(county_state+"#"+String.valueOf(resultarr[i])+"#"+
                    String.valueOf(varSlope_Change[i]));
        }
        int summ=0;
        int average_slope_chge=0;
        for (int i = 0; i < 5; i++) {
            summ+=varSlope_Change[i];

        }
        average_slope_chge=summ/5;

        System.out.println(String.join(",",  String.valueOf(resultarr[0]),
                String.valueOf(resultarr[1]),String.valueOf(resultarr[2]),
                String.valueOf(resultarr[3]),String.valueOf(resultarr[4]),
                String.valueOf(infection_num),String.valueOf(average_slope_chge)));


    }

    public static double[] predict (ArrayList<String[]> k, int infections, int deaths){
        double[] resultarr= {0,0,0,0,0};

        double[] slope={0,0,0,0,0};
        double[] intercept={0,0,0,0,0};
        double[] sumxy={0,0,0,0,0};
        double[] sumx={0,0,0,0,0};
        double[] sumy={0,0,0,0,0};
        double[] sumxsquare={0,0,0,0,0};
//        for (int i = 0; i < k.size(); i++) {
//            for (int j = 0; j < k.get(i).length; j++) {
//                System.out.println(k.get(i)[j]);
//            }
//        }


        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                double x=Double.valueOf(k.get(i)[5]);
                double y=Double.valueOf(k.get(i)[j]);
                sumxy[j]+=x*y;
               sumx[j]+=x;
               sumy[j]+=y;
               sumxsquare[j]+=x*x;
            }
        }
        double N= ((double) k.size());
        for (int i = 0; i < 5; i++) {
            slope[i]=(N * sumxy[i]-sumx[i]*sumy[i])/(N*sumxsquare[i]-sumx[i]*sumx[i]);
            intercept[i]=(sumy[i]-slope[i]*sumx[i])/N;
        }

        for (int i = 0; i < resultarr.length; i++) {
            resultarr[i]=slope[i] * 2022.0 + intercept[i];
        }
//        System.out.println(slope[4]);
//        System.out.println(sumx[4]);
//        System.out.println(intercept[4]);
//        for (int i = 0; i < resultarr.length; i++) {
//            System.out.println(resultarr[i]);
//        }

        return resultarr;
    }
    public static double[] evaluate(ArrayList<String[]> k, int infections, int deaths){
        double[] results={0,0,0,0,0};

        return results;
    }




}
//        for (Enumeration i =k.keys(); i.hasMoreElements();){
//            for (int j = 0; j < 5; j++) {
//                Object currobj=i.nextElement();
//                String[] currarr= (String[]) k.get(currobj);
//                int currkeydouble=(Integer) currobj;
//               sumxy[j]+=currkeydouble* Double.valueOf(currarr[j]);
//               sumx[j]+=currkeydouble;
//               sumy[j]+=Double.valueOf(currarr[j]);
//               sumxsquare[j]+=currkeydouble*currkeydouble;
//            }
//        }
