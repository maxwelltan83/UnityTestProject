using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class BoxCollider2DTests {
    private BoxCollider2D boxCollider2D;

    [SetUp]
    public void SetUp() {
        boxCollider2D = GameObject.Find("Player").GetComponent<BoxCollider2D>();
    }

    [Test]
    public void TestBounciness() {
        PhysicsMaterial2D increaseBouncing = new PhysicsMaterial2D();
        increaseBouncing.bounciness = 0.8f;
        boxCollider2D.sharedMaterial = increaseBouncing;
        Assert.AreEqual(0.8f, boxCollider2D.bounciness);
    }

    [Test]
    public void TestFriction() {
        PhysicsMaterial2D increaseFriction = new PhysicsMaterial2D();
        increaseFriction.friction = 1.0f;
        boxCollider2D.sharedMaterial = increaseFriction;
        Assert.AreEqual(1.0f, boxCollider2D.friction);
    }

    [Test]
    public void TestBoundSize() {
        boxCollider2D.size = new Vector3(2, 2, 0);;
        Assert.AreEqual(new Vector3(2, 2, 0), boxCollider2D.bounds.size);
    }

    [Test]
    public void TestBoundExtents() {
        Vector3 oldSize = boxCollider2D.bounds.size;
        boxCollider2D.size = new Vector3(2, 2, 0);
        Assert.AreEqual(new Vector3(1, 1, 0), boxCollider2D.bounds.extents);

        // reset size back to original
        boxCollider2D.size = oldSize;
    }

    // using [Timeout(2000)] does not seen to work 
    // so I implement my custom dynamic timeout
    [UnityTest]
    public IEnumerator TestBoundsIntersects() {
        yield return new EnterPlayMode(); 
        BoxCollider2D platformCollider = GameObject.Find("Platform").GetComponent<BoxCollider2D>();

        // Setup Dynamic Timeout Assertion
        // Check the value for duration of 2 second otherwise it will timeout
        // If assert pass before timeout end it will break the while loop
        float timeoutInMs = 2000f;
        float startTime = Time.realtimeSinceStartup;
        float endTime = 0f;
        while (endTime <= timeoutInMs) {
            yield return null;

            // The the value are equal
            if (boxCollider2D.bounds.Intersects(platformCollider.bounds)) {
                break;
            }
            endTime = (Time.realtimeSinceStartup - startTime) * 1000f;
        }
        
        // Throw error if timeout
        if (endTime > timeoutInMs) {
            Debug.LogError("Error message: TestBoundsIntersects when timeout -> expected = true but receive false");
        }

        Assert.IsTrue(boxCollider2D.bounds.Intersects(platformCollider.bounds));
    }
}
