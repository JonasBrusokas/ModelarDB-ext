/* Copyright 2021 The ModelarDB Contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package dk.aau.modelardb.engines.h2

import dk.aau.modelardb.core.SegmentGroup
import dk.aau.modelardb.storage.Storage
import org.h2.table.TableFilter

trait H2Storage extends Storage {
  def storeSegmentGroups(segments: Array[SegmentGroup], length: Int): Unit
  def getSegmentGroups(filter: TableFilter): Iterator[SegmentGroup]
}
