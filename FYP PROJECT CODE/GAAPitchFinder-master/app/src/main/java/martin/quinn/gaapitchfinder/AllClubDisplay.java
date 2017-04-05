package martin.quinn.gaapitchfinder;

import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import java.sql.SQLException;

public class AllClubDisplay extends AddClub{

    MyCursorAdapter cursorAdapter;

    private static final int CLUB = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_all_club_display);

        //this sends The name and id of a certain club
        Intent intent = getIntent();
        int countyID = intent.getIntExtra("countyID", 0);
        String clubInfo = intent.getStringExtra("clubInfo");

        final ListView listClubs = (ListView) findViewById(R.id.listView_clubs);

        // If the intent comes from CountyDisplay.java this will be executed
        if(countyID>0){
            try {
                db.open();
                //this searches a club with the id of a certain county
                Cursor result = db.getClub(countyID);
                cursorAdapter = new MyCursorAdapter(AllClubDisplay.this, result);

                listClubs.setAdapter(cursorAdapter);
                db.close();
            } catch (SQLException ex) {
                // If there is an error opening database
                ex.printStackTrace();
                Context context = getApplicationContext();
                int duration = Toast.LENGTH_LONG;
            }

            // If the intent is coming from SearchActivity.java this will be executed
        }else if (clubInfo != null) {
            try {
                db.open();
                //This Gets the club names with the closest to the inputted field
                Cursor result = db.getClubNames(clubInfo);

                cursorAdapter = new MyCursorAdapter(AllClubDisplay.this, result);
                listClubs.setAdapter(cursorAdapter);
                db.close();
            }
            catch (SQLException ex) {
                // If there is an error opening database
                ex.printStackTrace();
                Context context = getApplicationContext();
                int duration = Toast.LENGTH_LONG;
            }

            // if both "clubInfo" and "CountyID" are null
            // this will execute to display all clubs in the database
            } else {
                try {
                    db.open();
                    // This gets all the Clubs in the database
                    Cursor result = db.getAll();
                    cursorAdapter = new MyCursorAdapter(AllClubDisplay.this, result);
                    listClubs.setAdapter(cursorAdapter);
                    db.close();
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }

        // When a club is clicked / tapped
        listClubs.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> av, View view, int position, long arg) {

                // This is the information that gets passed to the club info activity which
                // displays the name, county, and location of the club in question

                Cursor cursor = (Cursor)cursorAdapter.getItem(position);
                String locQuery = cursor.getString(cursor.getColumnIndex("location"));
                String clubQuery = cursor.getString(cursor.getColumnIndex("club_name"));

                // starting the ClubInfo activity
                Intent ClubInfoDisplay = new Intent(AllClubDisplay.this, ClubInfo.class);
                Bundle extras = new Bundle();

                // Putting forward the two pieces of information
                extras.putString("clubInfo",clubQuery);
                extras.putString("locInfo",locQuery);
                ClubInfoDisplay.putExtras(extras);
                startActivityForResult(ClubInfoDisplay,CLUB);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_all_club_display, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if(requestCode == CLUB && resultCode ==RESULT_OK) {
            finish();
        }
    }
}

